#FUNCIONES OPCIONALES

def mostrar_onda(y, sr, save_path="forma_onda.png"):
    """
    Visualiza la forma de onda del audio y la guarda como imagen PNG.

    Args:
        y (np.ndarray): Señal de audio
        sr (int): Frecuencia de muestreo
        save_path (str): Ruta donde guardar la imagen PNG
    """
    plt.figure(figsize=(10, 3))
    librosa.display.waveshow(y, sr=sr)
    plt.title("Forma de onda - Audio de entrada (sin procesar)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.tight_layout()

    # Guardar como imagen en vez de mostrar en pantalla
    plt.savefig(save_path)
    plt.close()  # Cerrar para liberar memoria

    print(f"Forma de onda guardada en: {save_path}")


def show_mfcc(mfcc_features, title="Coeficiente MFCC 1 a lo largo del tiempo"):
    plt.figure(figsize=(10, 4))
    plt.plot(mfcc_features[:, 0])
    plt.title(title)
    plt.xlabel("Frames (1 cada 0.5s)")
    plt.ylabel("Valor del coeficiente 1")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("mfcc_coef1.png") 