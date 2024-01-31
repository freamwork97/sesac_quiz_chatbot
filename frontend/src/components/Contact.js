function Contact() {
  return (
    <div className="p-4 w-3/4 m-auto">
      <h2 className="text-2xl font-bold mb-4 text-center">개발자 프로필</h2>
      <div className="border border-gray-200 rounded-lg p-8">
        <div className="text-center mb-4">
          <img
            src={`https://picsum.photos/300/200?random=${Math.floor(
              Math.random() * 100
            )}`}
            alt="Developer"
            className="inline-block rounded-full w-64 h-64"
          />
          <h3 className="text-xl font-semibold mt-2">최도봉</h3>
          <p>LLM 개발자 </p>
        </div>
        <div className="mb-4">
          <h4 className="text-lg font-semibold">개발자 소개</h4>
          <p>저는 도봉이 개발자 입니다. 만나서 반가워요.</p>
        </div>
        <div className="mb-4">
          <h4 className="text-lg font-semibold">기술 스택</h4>
          <p>Python, FastAPI, HTML, CSS, JavaScript, React, LLM...</p>
        </div>
        <div className="mb-4">
          <h4 className="text-lg font-semibold">경력</h4>
          <p>Company ABC - Frontend Developer (2020-Present)</p>
          <p>Company XYZ - Web Developer Intern (2018-2020)</p>
        </div>
        <div>
          <h4 className="text-lg font-semibold">연락처</h4>
          <p>Email: dobong@email.com</p>
          <p>LinkedIn: linkedin.com/in/dobong</p>
        </div>
      </div>
    </div>
  );
}

export default Contact;
