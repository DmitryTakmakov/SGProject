from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


from post.models import Post


class PostEditForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        model = Post
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'user_id':
                field.widget = forms.HiddenInput()
            if field_name == 'hub_category':
                field.widget.attrs['required'] = True


