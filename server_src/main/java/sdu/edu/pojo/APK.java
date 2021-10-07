package sdu.edu.pojo;

import java.util.Date;

public class APK {
    private String MD5;
    private String name;
    private double size;
    private double RiskLevel;
    private double API_score;
    private double permission_score;
    private double behavior_scores;
    private String[] permission;
    private String[] Risk_Function;
    private String[] Activities;
    private String[] TelephonyIdentifiersLeakage;
    private String[] DeviceSettingsHarvesting;
    private String[] LocationLookup;
    private String[] ConnectionInterfacesExfiltration;
    private String[] TelephonyServicesAbuse;
    private String[] PimDataLeakage;
    private String[] SuspiciousConnectionEstablishment;
    private String[] AudioVideoEavesdropping;
    private String[] CodeExecution;
    private String UploadDate;
    private String status;
    private String packagename;
    private String MinSdkVersion;


    public double getBehavior_scores() {
        return behavior_scores;
    }

    public void setBehavior_scores(double behavior_scores) {
        this.behavior_scores = behavior_scores;
    }

    public String[] getCodeExecution() {
        return CodeExecution;
    }

    public void setCodeExecution(String[] codeExecution) {
        CodeExecution = codeExecution;
    }


    public String[] getTelephonyIdentifiersLeakage() {
        return TelephonyIdentifiersLeakage;
    }

    public void setTelephonyIdentifiersLeakage(String[] telephonyIdentifiersLeakage) {
        TelephonyIdentifiersLeakage = telephonyIdentifiersLeakage;
    }

    public String[] getDeviceSettingsHarvesting() {
        return DeviceSettingsHarvesting;
    }

    public void setDeviceSettingsHarvesting(String[] deviceSettingsHarvesting) {
        DeviceSettingsHarvesting = deviceSettingsHarvesting;
    }

    public String[] getLocationLookup() {
        return LocationLookup;
    }

    public void setLocationLookup(String[] locationLookup) {
        LocationLookup = locationLookup;
    }

    public String[] getConnectionInterfacesExfiltration() {
        return ConnectionInterfacesExfiltration;
    }

    public void setConnectionInterfacesExfiltration(String[] connectionInterfacesExfiltration) {
        ConnectionInterfacesExfiltration = connectionInterfacesExfiltration;
    }

    public String[] getTelephonyServicesAbuse() {
        return TelephonyServicesAbuse;
    }

    public void setTelephonyServicesAbuse(String[] telephonyServicesAbuse) {
        TelephonyServicesAbuse = telephonyServicesAbuse;
    }

    public String[] getPimDataLeakage() {
        return PimDataLeakage;
    }

    public void setPimDataLeakage(String[] pimDataLeakage) {
        PimDataLeakage = pimDataLeakage;
    }

    public String[] getSuspiciousConnectionEstablishment() {
        return SuspiciousConnectionEstablishment;
    }

    public void setSuspiciousConnectionEstablishment(String[] suspiciousConnectionEstablishment) {
        SuspiciousConnectionEstablishment = suspiciousConnectionEstablishment;
    }

    public String[] getAudioVideoEavesdropping() {
        return AudioVideoEavesdropping;
    }

    public void setAudioVideoEavesdropping(String[] audioVideoEavesdropping) {
        AudioVideoEavesdropping = audioVideoEavesdropping;
    }

    public String getMinSdkVersion() {
        return MinSdkVersion;
    }

    public double getAPI_score() {
        return API_score;
    }

    public void setAPI_score(double API_score) {
        this.API_score = API_score;
    }

    public double getPermission_score() {
        return permission_score;
    }

    public void setPermission_score(double permission_score) {
        this.permission_score = permission_score;
    }

    public void setMinSdkVersion(String minSdkVersion) {
        MinSdkVersion = minSdkVersion;
    }


    public String getMD5() {
        return MD5;
    }

    public void setMD5(String MD5) {
        this.MD5 = MD5;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getSize() {
        return size;
    }

    public void setSize(double size) {
        this.size = size;
    }

    public double getRiskLevel() {
        return RiskLevel;
    }

    public void setRiskLevel(double riskLevel) {
        RiskLevel = riskLevel;
    }

    public String[] getPermission() {
        return permission;
    }

    public void setPermission(String[] permission) {
        this.permission = permission;
    }

    public String[] getRisk_Function() {
        return Risk_Function;
    }

    public void setRisk_Function(String[] risk_Function) {
        Risk_Function = risk_Function;
    }

    public String[] getActivities() {
        return Activities;
    }

    public void setActivities(String[] activities) {
        Activities = activities;
    }

    public String getUploadDate() {
        return UploadDate;
    }

    public void setUploadDate(String uploadDate) {
        UploadDate = uploadDate;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getPackagename() {
        return packagename;
    }

    public void setPackagename(String packagename) {
        this.packagename = packagename;
    }
}
