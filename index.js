async function start() {
    const textarea = document.querySelector("textarea");
    const resultDiv = document.querySelector(".result");
  
    // Load the TFLite model.
    const model = await tfTask.NLClassification.CustomModel.TFLite.load({
      model:
        "https://storage.googleapis.com/tfweb/models/movie_review_sentiment_classification.tflite"
    });
  
    document.querySelector(".btn").addEventListener("click", async () => {
      // Get the classification result for the entered text
      const result = await model.predict(textarea.value);
  
      // Show the results.
      resultDiv.textContent = result.classes
        .map((c) => `${c.className}: ${c.score.toFixed(3)}`)
        .join(", ");
    });
  }
  
  start();
  