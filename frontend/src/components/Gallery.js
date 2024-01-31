const Gallery = () => {
  const imageUrls = [
    "https://picsum.photos/200?random=1",
    "https://picsum.photos/200?random=2",
    "https://picsum.photos/200?random=3",
    "https://picsum.photos/200?random=4",
    "https://picsum.photos/200?random=5",
    "https://picsum.photos/200?random=6",
    "https://picsum.photos/200?random=7",
    "https://picsum.photos/200?random=8",
    "https://picsum.photos/200?random=9",
    "https://picsum.photos/200?random=10",
    "https://picsum.photos/200?random=11",
    "https://picsum.photos/200?random=12",
    "https://picsum.photos/200?random=13",
    "https://picsum.photos/200?random=14",
  ];

  return (
    <>
      <h1 className="text-center text-3xl font-bold mb-4">Gallery</h1>
      <div className="text-center my-4 border border-black flex flex-wrap justify-center w-2/3 m-auto">
        {imageUrls.map((url, index) => (
          <img
            key={index}
            src={url}
            alt={`Gallery Item ${index + 1}`}
            className="w-48 m-2 transition-transform duration-300 hover:scale-110"
          />
        ))}
      </div>
    </>
  );
};

export default Gallery;
