from Crypto.PublicKey import RSA

def create_rsa_pair(is_save=False):
    '''
    创建rsa公钥私钥对
    :param is_save: default:False
    :return: public_key, private_key
    '''
    f = RSA.generate(2048)
    private_key = f.exportKey("PEM")  # 生成私钥
    public_key = f.publickey().exportKey()  # 生成公钥
    if is_save:
        with open("crypto_private_key.pem", "wb") as f:
            f.write(private_key)
        with open("crypto_public_key.pem", "wb") as f:
            f.write(public_key)
    return public_key, private_key
print(create_rsa_pair(True))


def read_public_key(file_path="crypto_public_key.pem") -> bytes:
    with open(file_path, "rb") as x:
        b = x.read()
        return b




def read_private_key(file_path="crypto_private_key.pem") -> bytes:
    with open(file_path, "rb") as x:
        b = x.read()
        return b
print(f"Key Pem output successsfully")
