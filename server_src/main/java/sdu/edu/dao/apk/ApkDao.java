package sdu.edu.dao.apk;

import sdu.edu.dao.BaseDao;
import sdu.edu.pojo.APK;

import java.sql.*;
import java.util.Arrays;

public class ApkDao {
    public APK GetApk(Connection connection, String MD5){
        PreparedStatement pstm = null;
        ResultSet rs = null ;
        APK apk =null;
        if(connection!=null){
            String sql = "select * from apk_db where MD5=?";
            Object[] params = {MD5};
            try {
                rs = BaseDao.execute(connection,sql,params,rs,pstm);
                if(rs.next()){
                    apk = new APK();
                    apk.setMD5(rs.getString("MD5"));
                    apk.setName(rs.getString("name"));
                    apk.setSize(rs.getDouble("size"));
                    apk.setPermission(rs.getString("permission").replace("[", "").replace("]", "").split(", "));
                    apk.setRisk_Function(rs.getString("Risk_Function").replace("[", "").replace("]", "").split(", "));
                    apk.setActivities(rs.getString("Activities").replace("[", "").replace("]", "").split(", "));
                    apk.setTelephonyIdentifiersLeakage(rs.getString("TelephonyIdentifiersLeakage").replace("[", "").replace("]", "").split(", "));
                    apk.setDeviceSettingsHarvesting(rs.getString("DeviceSettingsHarvesting").replace("[", "").replace("]", "").split(", "));
                    apk.setLocationLookup(rs.getString("LocationLookup").replace("[", "").replace("]", "").split(", "));
                    apk.setConnectionInterfacesExfiltration(rs.getString("ConnectionInterfacesExfiltration").replace("[", "").replace("]", "").split(", "));
                    apk.setTelephonyServicesAbuse(rs.getString("TelephonyServicesAbuse").replace("[", "").replace("]", "").split(", "));
                    apk.setPimDataLeakage(rs.getString("PimDataLeakage").replace("[", "").replace("]", "").split(", "));
                    apk.setSuspiciousConnectionEstablishment(rs.getString("SuspiciousConnectionEstablishment").replace("[", "").replace("]", "").split(", "));
                    apk.setAudioVideoEavesdropping(rs.getString("AudioVideoEavesdropping").replace("[", "").replace("]", "").split(", "));
                    apk.setCodeExecution(rs.getString("CodeExecution").replace("[", "").replace("]", "").split(", "));
                    apk.setRiskLevel(rs.getDouble("RiskLevel"));
                    apk.setAPI_score(rs.getDouble("API_score"));
                    apk.setPermission_score(rs.getDouble("permission_score"));
                    apk.setUploadDate(rs.getString("UploadDate"));
                    apk.setBehavior_scores(rs.getDouble("behavior_scores"));
                    apk.setStatus(rs.getString("Status"));
                    apk.setPackagename(rs.getString("packagename"));
                    apk.setMinSdkVersion(rs.getString("MinSdkVersion"));
                }
                BaseDao.closeResource(null,pstm,rs);
            } catch (SQLException throwables) {
                throwables.printStackTrace();
            }

        }
        return apk;
    }
    public int SetApk(Connection connection,APK apk){
        PreparedStatement pstm =null;
        int UpdateRows = 0;
        if(connection != null){
            String sql = "INSERT INTO apk_db(MD5,name,size,status,RiskLevel,API_score,permission_score,behavior_scores,permission,Risk_Function,UploadDate,packagename,Activities,MinSdkVersion,TelephonyIdentifiersLeakage,DeviceSettingsHarvesting,LocationLookup,ConnectionInterfacesExfiltration,TelephonyServicesAbuse,PimDataLeakage,SuspiciousConnectionEstablishment,AudioVideoEavesdropping,CodeExecution) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ";
            Object[] params = {apk.getMD5(),apk.getName(),apk.getSize(),apk.getStatus(),apk.getRiskLevel(),apk.getAPI_score(),apk.getPermission_score(),apk.getBehavior_scores(),Arrays.toString(apk.getPermission()),Arrays.toString(apk.getRisk_Function()),
                    apk.getUploadDate(),apk.getPackagename(),Arrays.toString(apk.getActivities()),apk.getMinSdkVersion(),
                    Arrays.toString(apk.getTelephonyIdentifiersLeakage()),Arrays.toString(apk.getDeviceSettingsHarvesting()),Arrays.toString(apk.getLocationLookup()),
                    Arrays.toString(apk.getConnectionInterfacesExfiltration()),Arrays.toString(apk.getTelephonyServicesAbuse()),
                    Arrays.toString(apk.getPimDataLeakage()),Arrays.toString(apk.getSuspiciousConnectionEstablishment()),Arrays.toString(apk.getAudioVideoEavesdropping()),Arrays.toString(apk.getCodeExecution())};

            try {
                UpdateRows = BaseDao.execute(connection,sql,params,pstm);
            } catch (SQLException throwables) {
                throwables.printStackTrace();
            }
            BaseDao.closeResource(null,pstm,null);

        }
        return UpdateRows;
    }
}
