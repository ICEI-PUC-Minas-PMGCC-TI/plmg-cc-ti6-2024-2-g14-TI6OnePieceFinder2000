import React, { useState } from "react";
import WantedPoster from "./components/WantedPoster/WantedPoster.tsx";
import Handler from "./components/Handler/Handler.tsx";
import "./App.css";

function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [jsonResult, setJsonResult] = useState(null); // State to store the received JSON result

  const handleUploadClick = async () => {
    if (!selectedImage) {
      alert("Please select an image before uploading.");
      return;
    }

    const formData = new FormData();
    formData.append("image", selectedImage);

    try {
      const response = await fetch("http://54.81.167.53:5000/api/process", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const json = await response.json(); // Parse JSON response
        setJsonResult(json); // Update the state with the JSON result
        alert("Image processed successfully!");
      } else {
        console.error("Error uploading image:", response.statusText);
      }
    } catch (err) {
      console.error("Error communicating with the backend:", err);
    }
  };

  return (
    <>
      <Handler />
      <div className="app-background">
        <h1>Upload and Process Your Image</h1>
        <WantedPoster onImageSelect={setSelectedImage} />
        <button onClick={handleUploadClick}>Upload and Process</button>
        {jsonResult && (
          <div style={{ marginTop: "20px" }}>
            <h2>Processed Result:</h2>
            <p><strong>Episodio:</strong> {jsonResult.Episodio}</p>
            <p><strong>Segundos:</strong> {jsonResult.Segundos}</p>
          </div>
        )}
      </div>
    </>
  );
}

export default App;