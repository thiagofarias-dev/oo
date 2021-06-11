class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de R${} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def tranferencia(self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)
        self.comprovante(destino)

    def comprovante(self, destino):
        self.extrato()
        destino.extrato()

    # Getters and Setters
    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    @property
    def limite(self):
        print("limite")
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
