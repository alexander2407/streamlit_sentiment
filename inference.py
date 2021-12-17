def inference(model, input_text):
    output = model([input_text])
    return output
