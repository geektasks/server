class Server():

    client_dict ={}

    def sign_up(self, name, password, transport):
        self.client_dict[name] = transport