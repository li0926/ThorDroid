package sdu.edu.service;

import sdu.edu.dao.BaseDao;
import sdu.edu.dao.apk.ApkDao;
import sdu.edu.pojo.APK;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.Arrays;
import java.util.Date;

public class QueryService {

    //引入Dao层
    private ApkDao apkDao;
    public QueryService(){
        apkDao = new ApkDao();
    }

    public APK query(String MD5){
        Connection connection = null;
        APK apk =null;

        try {
            connection = BaseDao.getConnection();
            apk = apkDao.GetApk(connection,MD5);
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        finally {
            BaseDao.closeResource(connection,null,null);
        }
        return apk;
    }
    public int Add(APK apk){
        Connection connection = null;
        int UpdateRows = 0;
        try {
            connection = BaseDao.getConnection();
            UpdateRows =apkDao.SetApk(connection,apk);
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }finally {
            BaseDao.closeResource(connection,null,null);
        }
        return UpdateRows;
    }


}
