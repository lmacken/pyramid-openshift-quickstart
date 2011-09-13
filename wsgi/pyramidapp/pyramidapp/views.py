def view_root(context, request):
    return {'items':list(context), 'project':'pyramidapp'}

def view_model(context, request):
    return {'item':context, 'project':'pyramidapp'}
