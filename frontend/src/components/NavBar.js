const NavBar = () => {
  return (
    <aside className="sticky top-12 h-1/3 w-1/3 border border-gray-300 p-2.5">
      <h1 className="text-center border-b border-gray-300 font-extrabold">
        도봉이 친구들
      </h1>
      <ul className="list-none text-center">
        <li>
          <a
            href="#link1"
            className="block p-2.5 border-b border-gray-300 hover:bg-gray-100"
          >
            노원이
          </a>
        </li>
        <li>
          <a
            href="#link2"
            className="block p-2.5 border-b border-gray-300 hover:bg-gray-100"
          >
            남구
          </a>
        </li>
        <li>
          <a
            href="#link3"
            className="block p-2.5 border-b border-gray-300 hover:bg-gray-100"
          >
            북구북구
          </a>
        </li>
        <li>
          <a
            href="#link4"
            className="block p-2.5 border-b border-gray-300 hover:bg-gray-100"
          >
            산이
          </a>
        </li>
      </ul>
    </aside>
  );
};

export default NavBar;
