class APK:
    def __init__(self, RiskFunction=dict(),behavior_scores=0,MinSdkVersion='', Permission=list(), Activities=list(), API_score=0,
                 permission_score=0, PackageName='', Status='', TelephonyIdentifiersLeakage=list(),
                 DeviceSettingsHarvesting=list(), LocationLookup=list(), ConnectionInterfacesExfiltration=list(),
                 TelephonyServicesAbuse=list(), PimDataLeakage=list(), SuspiciousConnectionEstablishment=list(),
                 AudioVideoEavesdropping=list(), CodeExecution=list()):
        self.RiskFunction = RiskFunction
        self.Permission = Permission
        # 修改了这里
        self.API_score = API_score
        self.permission_score = permission_score
        self.RiskLevel = lambda x,y: (x+y)/2
        self.PackageName = PackageName
        self.Status = Status
        self.Activities = Activities
        self.MinSdkVersion = MinSdkVersion
        self.TelephonyIdentifiersLeakage = TelephonyIdentifiersLeakage
        self.DeviceSettingsHarvesting = DeviceSettingsHarvesting
        self.LocationLookup = LocationLookup
        self.ConnectionInterfacesExfiltration = ConnectionInterfacesExfiltration
        self.TelephonyServicesAbuse = TelephonyServicesAbuse
        self.PimDataLeakage = PimDataLeakage
        self.SuspiciousConnectionEstablishment = SuspiciousConnectionEstablishment
        self.AudioVideoEavesdropping = AudioVideoEavesdropping
        self.CodeExecution = CodeExecution
        self.behavior_scores = behavior_scores

    def todict(self):
        data = dict()
        data['behavior_scores'] = self.behavior_scores
        data['RiskFunction'] = self.RiskFunction
        data['Permission'] = self.Permission
        data['RiskLevel'] = int(self.RiskLevel(self.API_score,self.permission_score))
        data['API_score'] = self.API_score
        data['permission_score'] = self.permission_score
        data['PackageName'] = self.PackageName
        data['Status'] = self.Status
        data['Activities'] = self.Activities
        data['MinSdkVersion'] = self.MinSdkVersion
        data['TelephonyIdentifiersLeakage'] = self.TelephonyIdentifiersLeakage
        data['DeviceSettingsHarvesting'] = self.DeviceSettingsHarvesting
        data['LocationLookup'] = self.LocationLookup
        data['ConnectionInterfacesExfiltration'] = self.ConnectionInterfacesExfiltration
        data['TelephonyServicesAbuse'] = self.TelephonyServicesAbuse
        data['PimDataLeakage'] = self.PimDataLeakage
        data['SuspiciousConnectionEstablishment'] = self.SuspiciousConnectionEstablishment
        data['AudioVideoEavesdropping'] = self.AudioVideoEavesdropping
        data['CodeExecution'] = self.CodeExecution
        return data
