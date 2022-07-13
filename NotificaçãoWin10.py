from win10toast import ToastNotifier

#inicializa 
toaster = ToastNotifier ()

#passa parâmetros e mostra a notificação 
toaster.show_toast(
    "Um DEV detectado!",
    "Você acessou meu repositorio, sinta-se a vontade aqui!",
    threaded=True,
    icon_path=None,
    duration=10
)

