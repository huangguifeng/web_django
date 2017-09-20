class MiddleWare(object):
    def process_view(self,request,views_func,view_args,view_kwargs):
        if request.path not in ['/user/register/','/user/login/','/useer/namebj/','/user/emailbj/','/user/create/'
                    ,'/user/namech/','/user/user_login/','/user/verify_code/', '/user/center_info/',  '/user/center_order/',
                            '/user/center_site/', '/user/user_addr/logout/']:
            request.session['url_path']=request.get_full_path()
