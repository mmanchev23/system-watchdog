import axios from "axios";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";

interface Host {
  id: string;
  name: string;
}

const Hosts = () => {
  const [hosts, setHosts] = useState<Host[]>([]);

  const fetchHosts = async () => {
    try {
      const response = await axios.get<{ hosts: Host[] }>("http://localhost:8000/hosts/");
      setHosts(response.data.hosts);
    } catch (error) {
      console.log(error);
    }
  }

  useEffect(() => {
    fetchHosts();
  }, []);

  return (
    <div className="container mt-5">
      <h1 className="mb-4">Hosts</h1>
      <ul className="list-group">
        {hosts && hosts.length > 0 ? hosts.map((host) => (
          <li key={host.id} className="list-group-item">
            <Link to={`/${host.id}`}>{host.name}</Link>
          </li>
        )) : (
          <li className="list-group-item">
            No hosts have been registered yet ...
          </li>
        )}
      </ul>
    </div>
  );
};

export default Hosts;
