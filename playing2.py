from imageai.Prediction.Custom  import ModelTraining

model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory("idenprof")
model_trainer.trainModel(num_objects=1, num_experiments=200,batch_size=32)


