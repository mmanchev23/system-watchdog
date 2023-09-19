import { useState, SyntheticEvent } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const CreateHost = () => {
  const [hostName, setHostName] = useState<string>("");
  const navigate = useNavigate();

  const handleFormSubmit = async (e: SyntheticEvent) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://localhost:8000/hosts/", { name: hostName });
      navigate(`/${response.data.host.id}`);
      console.log(response.data.message);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="container mt-5">
      <h1>Create Host</h1>
      <form onSubmit={handleFormSubmit}>
        <div className="form-group">
          <label>Host Name</label>
          <input
            type="text"
            className="form-control"
            value={hostName}
            onChange={(e) => setHostName(e.target.value)}
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Create
        </button>
      </form>
    </div>
  );
};

export default CreateHost;
