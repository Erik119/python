

class Ams:
    def __init__(self):
        self.name = "ams"
        self.downtime = 0
        self.servers = {}
        self.virtual_ip = None
        self.virtual_ip_host = None
        self.geo = self._Geo_cluster()

    class _Server:
        ams_build = []
        ems_ef_version = []
        master = False

    def testit(self, data):
        self._parse_cluster_data(data)


    def _parse_cluster_data(self, cluster_data):
        '''_parse_cluster_data:
        process cluster data file and '''
        site = None
        for line in cluster_data.split('\n'):
            if 'Site:' in line or 'Remote site:' in line:
                if '(Active)' in line:
                    site = self.geo.active
                elif '(Standby' in line:
                    site = self.geo.standby
                site.site_name = line.split()[-2]
            if 'Status:' in line:
                site.status = line.split()[-1]
            if 'slacrr' in line:
                name = line.split()[0]
                server = site._Server(line.split())
                site.servers.update({name:server})
        print(self.geo.active.status)
        print(self.geo.standby.status)

    class _Geo_cluster:
        def __init__(self):
            self.active = self._Cluster()
            self.standby = self._Cluster()

        class _Cluster:
            def __init__(self):
                self.servers = {}
                self.status = ""
                self.site_name = None

            class _Server:
                def __init__(self, data):
                    self.name = data[0]
                    self.role = data[1]
                    self.health = data[2]
                    self.ams = data[3]
                    self._as = data[4]
                    self.db = data[5]
                    self.pm = data[6]
                    self.service = data[7]

data = '''
Started on Thu Jul 23 12:20:58 2020
Running since 6 days and 21:12:27


Last update:   Wed Jul 29 08:55:04 2020
=============================================================================
Site:          Production_AMS-cluster_Asd (Active)
Type:          Cluster
Status:        Healthy
=============================================================================
Server Name Role     Health   AMS      AS       DB       PM       Service
-----------------------------------------------------------------------------
slacrr169   A+a      H        R        R        -        R        R
slacrr170   A        H        R        RM       -        R        R
slacrr171   A        H        R        R        -        R        R
slacrr172   A        H        R        R        -        R        R
slacrr167   D        H        -        -        SL       R        R
slacrr168   D        H        -        -        M        R        R


Last update:   Wed Jul 29 08:54:53 2020
=============================================================================
Remote site:   Production_AMS-cluster_Rt (Standby)
Type:          Cluster
Status:        Health
=============================================================================
Server Name Role     Health   AMS      AS       DB       PM       Service
-----------------------------------------------------------------------------
slacrr175   A        DG       W        W        -        R        R
slacrr176   A+a      DG       W        W        -        R        R
slacrr177   A        DG       W        W        -        R        R
slacrr178   A        DG       W        W        -        R        R
slacrr173   D        H        -        -        SL       R        R
slacrr174   D        H        -        -        SL       R        R
'''

ams = Ams()
ams.testit(data)
print(ams.geo.active.site_name)
print(ams.geo.active.servers)
print(ams.geo.standby.site_name)
print(ams.geo.standby.servers)

for server,value in ams.geo.active.servers.items():
    print(server)
    print(getattr(value, 'health'))
    print(getattr(value, 'role'))
#    health = getattr(ams.geo.active.servers)
#    print('getattr ' + getattr(ams.geo.active.servers.server, name))

print(80*'=')
print(getattr(ams.geo.active.servers['slacrr169'], 'health', "niets"))
# deze werkt niet print(ams.geo.active.servers['slacrr169'].'health')
