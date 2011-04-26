from libcloud.drivers.ec2 import EC2Connection, EC2NodeDriver

class NimbusConnection(EC2Connection):

    host = ''
    port = (80, 8444)
    secure = 1

class NimbusNodeDriver(EC2NodeDriver):

    connectionCls = NimbusConnection
    name = "Nimbus"

    def __init__(self, *args, **kwargs):
        self.fix_xpath = not kwargs.pop('ex_oldnimbus_xml', False)
        EC2NodeDriver.__init__(self, *args, **kwargs)

    def _fixxpath(self, xpath):
        # old (pre 2.7) Nimbus return types don't include namespace declaration in every
        # tag, unlike EC2. So we override this method to make xpath queries
        # just pass through instead of being ns-prefixed.

        if self.fix_xpath:
            return EC2NodeDriver._fixxpath(self, xpath)
        else:
            return xpath
