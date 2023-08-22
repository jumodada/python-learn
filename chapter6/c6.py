# 法定结婚年龄的限制，比如男22岁，女20岁

class AgeError(Exception):...
    # pass

class Person():
    def set_age(self,age):
        raise AgeError("你必须覆盖set_age方法，进行你自己的年龄控制")

class Boy(Person):
    def set_age(self, age):
        if age < 22:
            raise AgeError("男孩的年龄不能小于22岁")
        else:
            self.age = age

class Girl(Person):
    def set_age(self, age):
        if age < 20:
            raise AgeError("女孩的年龄不能小于20岁")
        else:
            self.age = age

boy = Boy()
boy.set_age(22)
girl = Girl()
girl.set_age(18)