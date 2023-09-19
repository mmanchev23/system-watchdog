import { Routes, Route } from "react-router-dom";

import Navigation from "./Shared/Navbar";

import Hosts from "./Hosts/Hosts";
import Host from "./Hosts/Host";
import CreateHost from "./Hosts/CreateHost";
import EditHost from "./Hosts/EditHost";

const App = () => {
  return (
    <div>
      <Navigation />
      <div className="container mt-4">
        <Routes>
          <Route path="/" element={<Hosts />} />
          <Route path="/:id" element={<Host />} />
          <Route path="/create" element={<CreateHost />} />
          <Route path="/:id/edit" element={<EditHost />} />
        </Routes>
      </div>
    </div>
  );
};

export default App;
