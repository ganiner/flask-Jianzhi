;
var user_login_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $(".login_wrap .do-login").click( function(){

            var btn_target = $(this);
            if( btn_target.hasClass("disabled") ){
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }

            var login_name =  $(".login_wrap input[name=username]").val();
            var login_pwd  =   $(".login_wrap input[name=password]").val();
            var login_codes = $(".login_wrap input[name=vercode]").val();


            if( login_name == undefined || login_name.length < 1){
                common_ops.alert( "请输入正确的登录用户名或密码" );
                return;
            }
            if( login_pwd == undefined || login_pwd.length < 1){
                common_ops.alert( "请输入正确的登录用户名或密码" );
                return;
            }
            if( login_codes == undefined || login_codes.length < 1 ){
                common_ops.alert( "请输入正确的验证码" );
                return;
            }
            btn_target.addClass("disabled");
            //取消默认事件的处理。也就是说阻止访问href中的网页,下面的作用
            // window.event.returnValue=false
            $.ajax({
                url:"http://127.0.0.1:5000/login/",
                // url:common_ops.buildUrl("/login/"),
                type:'POST',
                async:false,
                data:{ 'username':login_name,'password':login_pwd,'codes':login_codes },
                dataType:'json',
                success:function(res){
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if( res.code == 200 ){
                            location.href="http://127.0.0.1:5000/jianzhi/"
                        callback = function(){
                            window.location.href="http://127.0.0.1:5000/jianzhi/"

                        }
                    }
                    if (res.code==-1){
                        callback=function () {
                            $("#codes").attr('src',common_ops.buildUrl("/login/code?"+Math.random()));
                        }
                    }

                    common_ops.alert( res.msg,callback );
                }
            });
        } );
    }
};




$(document).ready( function(){
    user_login_ops.init();
} );