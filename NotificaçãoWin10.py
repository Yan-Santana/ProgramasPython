from win10toast import ToastNotifier

toaster = ToastNotifier ()
toaster.show_toast(
    "Um DEV detectado!",
    "Você acessou meu repositorio, sinta-se a vontade aqui!",
    threaded=True,
    icon_path=None,
    duration=10
)
