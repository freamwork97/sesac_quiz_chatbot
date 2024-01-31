import NavBar from "./NavBar";
import React, { useState } from "react";

const ChatRoom = () => {
  const [userInput, setUserInput] = useState("");
  const [chatHistory, setChatHistory] = useState([]);

  const handleInputChange = (e) => {
    setUserInput(e.target.value);
  };

  const sendMessage = async () => {
    const userMessage = userInput.trim();
    console.log(userMessage);
    if (!userMessage) return;

    // Add user message to chat history
    setChatHistory([...chatHistory, { sender: "User", message: userMessage }]);

    try {
      const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ user_input: userMessage }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const responseData = await response.json();
      console.log(responseData);
      setChatHistory((prevHistory) => [
        ...prevHistory,
        { sender: "도봉이", message: responseData.도봉이 },
      ]);
    } catch (error) {
      console.error("Error sending message:", error);
    }
    console.log(chatHistory);

    // Clear input field
    setUserInput("");
  };

  return (
    <section className=" flex flex-col">
      <h1 className="text-center text-3xl font-bold mb-4">도봉이와의 대화방</h1>
      <div className="w-full mx-auto my-4 max-w-2xl flex flex-row">
        <div className="w-full mx-auto max-w-3xl h-[80vh] pt-2 flex flex-row">
          <NavBar />
          <div className="w-full">
            <div className="h-[70%] w-full border border-gray-300 mb-4 p-2 overflow-y-scroll">
              {/* Display chat history */}
              {chatHistory.map((chat, index) => (
                <div
                  key={index}
                  className={`message ${
                    chat.sender === "User" ? "user" : "도봉이"
                  }`}
                >
                  <p>
                    <strong>{chat.sender}:</strong> {chat.message}
                  </p>
                </div>
              ))}
            </div>
            <div className="flex justify-between border-gray-300 border">
              <input
                type="text"
                value={userInput}
                onChange={handleInputChange}
                className="w-4/5 p-2"
                placeholder="메세지를 입력하세요."
                onKeyPress={(e) => e.key === "Enter" && sendMessage()}
              />
              <button
                onClick={sendMessage}
                className="w-1/5 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
              >
                보내기
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ChatRoom;
