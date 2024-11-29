import React, { useRef } from "react";

interface UploadButtonProps {
  onImageUpload: (file: File) => void;
}

const UploadButton: React.FC<UploadButtonProps> = ({ onImageUpload }) => {
  const fileInputRef = useRef<HTMLInputElement | null>(null);

  const buttonStyle: React.CSSProperties = {
    backgroundColor: "transparent", 
    color: "#5A4D3D",
    width: "300px", 
    height: "70px", 
    display: "flex",
    alignItems: "center", 
    justifyContent: "center", 
    fontSize: "22px",
    fontWeight: "bold",
    border: "none",
    cursor: "pointer",
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    zIndex: 3,  
    marginTop: "-30px"
  };

  const handleButtonClick = () => {
    if (fileInputRef.current) {
      fileInputRef.current.click();
    }
  };

  const handleImageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      onImageUpload(event.target.files[0]);
    }
  };

  return (
    <>
      <button
        style={buttonStyle}
        onClick={handleButtonClick}
      >
        Jogue sua imagem ou clique para subir
      </button>
      <input
        type="file"
        accept="image/*"
        ref={fileInputRef}
        style={{ display: "none" }}
        onChange={handleImageChange}
      />
    </>
  );
};

export default UploadButton;
