from config import Config

cf = Config()

print(cf.data.root)
print(cf.data.train)
print(cf.data.test)
print(cf.data.validation.path)
print(cf.data.validation.percentage)
print(cf.secrets)
print(cf.secrets.db['user'])
print(cf.secrets.db['password'])
print(cf.secrets.db['name'])
print(cf.secrets.host)
print(cf.secrets.port)
print(cf.train.epochs)
print(cf.train.batch_size)
print(cf.train.lr)
print(cf.train.callback)
print(cf.train.retrain)
print(cf.version)
print(cf.debug)

