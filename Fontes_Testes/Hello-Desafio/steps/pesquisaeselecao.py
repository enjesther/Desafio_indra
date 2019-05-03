@given(u'que o usuário está no site Americanas')
def step_impl(context):
    context.pesquisa.go_home()


@when(u'realiza uma pesquisa de Iphone')
def step_impl(context):
    context.pesquisa.fazer_pesquisa('Iphone')


@when(u'selecionar um dos produtos apresentados')
def step_impl(context):
    context.pesquisa.selecionar_produto()

@when(u'colocar no carrinho')
def step_impl(context):
    context.pesquisa.produto_no_carrinho()

@when(u'selecionar sem seguro')
def step_impl(context):
    context.pesquisa.sem_seguro()

@then(u'o sistema deve apresentar o produto selecionado no carrinho')
def step_impl(context):
    context.pesquisa.validacao()


