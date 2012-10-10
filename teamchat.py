# teamchat.py
# Shows team chat in IRC, colored appropriately.
# by topologist

def apply_script(protocol, connection, config):
    class TeamChatConnection(connection):
        def on_chat(self, value, is_global):
            if is_global or not self.protocol.irc_relay:
                return connection.on_chat(self, value, is_global)
            bold = False
            if self.team == self.protocol.blue_team:
                message = '<\x0302'
            elif self.team == self.protocol.green_team:
                message = '<\x0303'
            else:
                message = '<\x02'
                bold = True
            message += '%s%s> %s' % (self.name, '\x02' if bold else '\x03', value)
            self.protocol.irc_relay.send(message, filter = False)
            return connection.on_chat(self, value, is_global)
    return protocol, TeamChatConnection