from tensorflow import keras

(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1)).astype('float')/255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float')/255
train_labels = keras.utils.to_categorical(train_labels)
test_labels = keras.utils.to_categorical(test_labels)

model = keras.Sequential([
        keras.layers.Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
        keras.layers.AveragePooling2D((2, 2)),
        keras.layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu'),
        keras.layers.AveragePooling2D((2, 2)),
        keras.layers.Conv2D(filters=120, kernel_size=(3, 3), activation='relu'),
        keras.layers.Flatten(),
        keras.layers.Dense(84, activation='relu'),
        keras.layers.Dense(10, activation='softmax'),
])

model.compile(optimizer=keras.optimizers.RMSprop(lr=0.001), loss=keras.losses.categorical_crossentropy,
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10, batch_size=128, verbose=2)

test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print("损失:", test_loss, "精准度:", test_accuracy)


