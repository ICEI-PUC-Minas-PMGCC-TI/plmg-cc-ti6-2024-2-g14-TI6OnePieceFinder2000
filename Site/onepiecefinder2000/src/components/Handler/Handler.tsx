import React from "react";

const Header: React.FC = () => {
  const headerStyle: React.CSSProperties = {
    backgroundColor: "#CAA675",
    padding: "20px",
    textAlign: "left", 
    boxShadow: "0 2px 4px rgba(0, 0, 0, 0.2)", 
  };

  const titleStyle: React.CSSProperties = {
    fontSize: "36px",
    color: "#333", 
    margin: 0, 
  };

  return (
    <header style={headerStyle}>
      <h1 style={titleStyle}>One Piece Finder 2000</h1>
    </header>
  );
};

export default Header;
