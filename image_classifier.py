# File: image_classifier.py

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def train_model():
    """Trains a simple image classifier on a sample dataset."""
    # Data augmentation
    datagen = ImageDataGenerator(rescale=1.0/255, validation_split=0.2)

    train_data = datagen.flow_from_directory(
        'data/images',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary',
        subset='training'
    )

    val_data = datagen.flow_from_directory(
        'data/images',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary',
        subset='validation'
    )

    # Model definition
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train model
    model.fit(train_data, epochs=10, validation_data=val_data)

    # Save the trained model
    model.save('image_classifier.h5')
    print("Model saved as 'image_classifier.h5'")

if __name__ == '__main__':
    train_model()
