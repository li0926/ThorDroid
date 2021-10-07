package sdu.edu.servlet;

import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.FileUploadException;
import org.apache.commons.fileupload.ProgressListener;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;
import org.json.JSONObject;
import sdu.edu.pojo.APK;
import sdu.edu.service.QueryService;
import sdu.edu.tools.ApkCore;
import sdu.edu.tools.DeleteDirectory;
import sdu.edu.tools.Md5CaculateUtil;
import sdu.edu.tools.TempMD5;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.List;
import java.util.UUID;
import sdu.edu.tools.Verify;

public class UploadServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

            if (!ServletFileUpload.isMultipartContent(request)) {
                return;//终止方法运行,说明这是一个普通的表单,直接返回
            }
            //创建上传文件的保存路径,建议在WEB-INF路径下,安全,用户无法直接访间上传的文件;
            String uploadPath =this.getServletContext().getRealPath("/WEB-INF/upload");
            String pythonPath = this.getServletContext().getRealPath("/WEB-INF/thordroid/src");
            File uploadFile = new File(uploadPath);
            if (!uploadFile.exists()){
                uploadFile.mkdir(); //创建这个目录
            }

            // 创建上传文件的保存路径，建议在WEB-INF路径下，安全，用户无法直接访问上传的文件
            String tmpPath = this.getServletContext().getRealPath("/WEB-INF/tmp");
            File file = new File(tmpPath);
            if (!file.exists()) {
                file.mkdir();//创建临时目录
            }
            try {
                // 创建DiskFileItemFactory对象，处理文件路径或者大小限制
                DiskFileItemFactory factory = getDiskFileItemFactory(file);
                // 2、获取ServletFileUpload
                ServletFileUpload upload = getServletFileUpload(factory);


                // 3、处理上传文件
                // 把前端请求解析，封装成FileItem对象，需要从ServletFileUpload对象中获取
                TempMD5 tempMD5 = new TempMD5();
                String realPath = uploadParseRequest(upload, request, uploadPath,tempMD5);

                if(realPath.equals("")){
                    response.sendRedirect("main.jsp");
                    return;
                }

//            request.getSession().setAttribute("md5",tempMD5.getMd5());
//            response.sendRedirect("detail.jsp");
                //处理APK
                ProcessApk(realPath,pythonPath);
                //删除该目录
//            File file1 = new File(realPath);
//            DeleteDirectory.deleteDir(file1);


            } catch (FileUploadException e) {
                // TODO 自动生成的 catch 块
                e.printStackTrace();
                request.setAttribute("msg", "您上传的文件超出了100KB！");
                request.getRequestDispatcher("index.jsp").forward(request, response);
            }


    }


    /*
        给定文件的路径,计算该文件的md5值并判断是否已经存到数据库中
    */
    public static void ProcessApk(String uploadPath,String pythonPath){
        File file = new File(uploadPath);
        String filemd5 = "";
        QueryService queryService = new QueryService();
        APK apk=null;
        //每个文件夹下只有一个文件
        File[] listFiles = file.listFiles();
        filemd5 = Md5CaculateUtil.getMD5(listFiles[0]);

        apk =queryService.query(filemd5);
        if(apk==null){//为空,说明数据库中不存在该apk,处理该APK
            apk = ApkCore.HandleApk(file,pythonPath);
            queryService.Add(apk);
        }

    }


    public static DiskFileItemFactory getDiskFileItemFactory(File file) {
        //创建FileItem对象的工厂
        DiskFileItemFactory factory = new DiskFileItemFactory();
        // 通过这个工厂设置一个缓冲区,当上传的文件大于这个缓冲区的时候,将他放到临时文件中;
        factory.setSizeThreshold(1024 * 1024 * 100);// 缓冲区大小为100M
        factory.setRepository(file);// 临时目录的保存目录,需要一个file
        return factory;
    }

    public static ServletFileUpload getServletFileUpload(DiskFileItemFactory factory) {
        ServletFileUpload upload = new ServletFileUpload(factory);
        // 监听长传进度
        upload.setProgressListener(new ProgressListener() {

            // pBYtesRead:已读取到的文件大小
            // pContextLength:文件大小
            public void update(long pBytesRead, long pContentLength, int pItems) {
                System.out.println("File size: " + pContentLength + " Uploaded:" + pBytesRead);
            }
        });

        // 处理乱码问题
        upload.setHeaderEncoding("UTF-8");
        // 设置单个文件的最大值
        upload.setFileSizeMax(1024 * 1024 * 10);
        // 设置总共能够上传文件的大小
        // 1024 = 1kb * 1024 = 1M * 10 = 10м
        return upload;
    }

    public static String uploadParseRequest(ServletFileUpload upload, HttpServletRequest request, String uploadPath, TempMD5 tempMD5)
            throws FileUploadException, IOException {

        String realPath = "";
        List<FileItem> fileItems;
        // 把前端请求解析，封装成FileItem对象

        fileItems = upload.parseRequest(request);
        for (FileItem fileItem : fileItems) {
            if (fileItem.isFormField()) {// 判断上传的文件是普通的表单还是带文件的表单
                // getFieldName指的是前端表单控件的name;
                String name = fileItem.getFieldName();
                String value = fileItem.getString("UTF-8"); // 处理乱码
                System.out.println(name + ": " + value);
            } else {// 判断它是上传的文件

                // ============处理文件==============

                // 拿到文件名
                String uploadFileName = fileItem.getName();
                System.out.println("Upload file name : " + uploadFileName);
                if (uploadFileName.trim().equals("") || uploadFileName == null) {
                    continue;
                }

                // 获得上传的文件名/images/girl/paojie.png
                String fileName = uploadFileName.substring(uploadFileName.lastIndexOf("/") + 1);
                // 获得文件的后缀名
                String fileExtName = uploadFileName.substring(uploadFileName.lastIndexOf(".") + 1);

                System.out.println("filename: [" + fileName + " ---filetype: " + fileExtName + "]");
                // 可以使用UID（唯一识别的通用码),保证文件名唯一
                // UID. randomUUID(),随机生一个唯一识别的通用码;
                String uuidPath = UUID.randomUUID().toString();

                // ================处理文件==============
                // 存到哪? uploadPath
                // 文件真实存在的路径realPath
                realPath = uploadPath + "/" + uuidPath;
                // 给每个文件创建一个对应的文件夹
                File realPathFile = new File(realPath);
                if (!realPathFile.exists()) {
                    realPathFile.mkdir();
                }
                // ==============存放地址完毕==============


                // 获得文件上传的流
                InputStream inputStream = fileItem.getInputStream();
                // 创建一个文件输出流
                // realPath =真实的文件夹;
                FileOutputStream fos = new FileOutputStream(realPath + "/" + fileName);

                // 创建一个缓冲区
                byte[] buffer = new byte[1024 * 1024* 100];
                // 判断是否读取完毕
                int len = 0;
                // 如果大于0说明还存在数据;
                while ((len = inputStream.read(buffer)) > 0) {
                    fos.write(buffer, 0, len);
                }
                // 关闭流
                fos.close();
                inputStream.close();

                fileItem.delete(); // 上传成功,清除临时文件
                //=============文件传输完成=============

                //获取上传文件的MD5值
                tempMD5.setMd5(Md5CaculateUtil.getMD5(new File(realPath+"/"+fileName)));
            }
        }
        return realPath;
    }

}
