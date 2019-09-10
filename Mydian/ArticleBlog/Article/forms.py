from django import forms

class Register(forms.Form):
    username=forms.CharField(min_length=6,max_length=32,label="用户名:",required=True)
    password=forms.CharField(max_length=32,widget=forms.PasswordInput,label="密码:")
    email=forms.EmailField()
    def clean_username(self):
        """
        自定义校验函数的名字是固定的
        """
        username=self.cleaned_data.get("username")
        if username=="admin":
            self.add_error("username","用户不可以是:%s"%username)
        else:
            return username