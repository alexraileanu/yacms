from app import redis_instance
from redis import RedisError


class CMS(object):
    hash_key = 'yacms_settings'

    @classmethod
    def get(cls, key=None):
        if key:
            # safe to assume it will only return one value because when adding fields to this hash,
            # I never add more than one (I hope)
            return redis_instance.hmget(cls.hash_key, key)[0].decode()

        return redis_instance.hgetall(cls.hash_key)

    @classmethod
    def set(cls, field, value):
        print(field, value)
        return redis_instance.hset(cls.hash_key, field, value)

    def save(self):
        try:
            for set_attr in self.__dict__:
                if set_attr not in ['submit']:
                    self.set(set_attr, getattr(self, set_attr))

            msg, cat = 'Settings saved successfully', 'success'
        except RedisError:
            msg, cat = 'Error saving settings', 'error'

        return msg, cat
