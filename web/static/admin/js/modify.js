;

var modifys={
    init:function () {
        this.eventBind();
    },
    eventBind:function(){
        layui.use('layer', function(){
            var layer = layui.layer;
        layer.open({
        type: 1,
        title:'修改'+$(".tit_username").text(),
        anim:1,
        offset:'100px',
        area: ['720px', '300px'],
       content: '<input class="layui-input" id="new_input">' +
       '<button id="modfily" class="layui-btn">点击修改</button>',
});
    var name=$("#new_input").val();
     $.ajax({
         url:common_ops.buildUrl("/api/userMessage/"),
                type:'POST',
                data:{ 'username':name},
                dataType:'json',
                success:function(res){

                    var callback = null;
                    if( res.code == 200 ){
                        callback = layer.close(index);
                    }
                    if (res.code==-1){

                    }
                    common_ops.alert( res.msg,callback );
                }
     });
});
});

}



$("#modfily").click(
    function () {
        modifys.init()
    }
)








