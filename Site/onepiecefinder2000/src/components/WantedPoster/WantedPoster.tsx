import React, { useState } from "react";
import UploadButton from "../UploadButton/UploadButton.tsx";
import "./WantedPoster.css";

interface WantedPosterProps {
  onImageSelect: (file: File) => void;
}

const WantedPoster: React.FC<WantedPosterProps> = ({ onImageSelect }) => {
  const [uploadedImage, setUploadedImage] = useState<string | null>(null);

  const handleImageUpload = (file: File) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      if (e.target?.result) {
        setUploadedImage(e.target.result as string); // Set the uploaded image for display
        onImageSelect(file); // Pass the file to the parent for further handling
      }
    };
    reader.readAsDataURL(file); // Convert the file to a data URL for immediate display
  };

  return (
    <div className="mainContainerStyle">
      <img src="./img/luf-Photoroom.png" alt="Luffy Wanted Poster" className="imageStyle"/>

      <div className="posterContainerStyle">
        {uploadedImage && (
          <img src={uploadedImage} alt="Uploaded" className="uploadedImageStyle"
          />
        )}

        <img src="/img/cartazF.png" alt="Wanted Poster" className="posterStyle" />

        {!uploadedImage && <UploadButton onImageUpload={handleImageUpload} />}
      </div>
    </div>
  );
};

export default WantedPoster;