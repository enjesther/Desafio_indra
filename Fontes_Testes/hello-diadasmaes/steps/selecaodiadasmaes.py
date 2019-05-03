@given(u'que esteja na tela inicial da americanas')
def step_impl(context):
    context.maes.go_home()


@when(u'selecionado o menu dia das mães')
def step_impl(context):
    context.maes.menu_maes()


@when(u'selecionar a categoria Moda')
def step_impl(context):
    context.maes.categoria_moda()


@when(u'selecionar a categoria moda praia')
def step_impl(context):
    context.maes.moda_praia()


@when(u'selecionar o produto')
def step_impl(context):
    context.maes.seleciona_produto()


@then(u'deve ser apresentado a pagina do produto')
def step_impl(context):
    context.maes.verificacao()