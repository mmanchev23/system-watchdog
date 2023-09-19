import { useEffect, useState } from "react";
import axios from "axios";
import { useParams, useNavigate } from "react-router-dom";

const EditHost = () => {
  const { id } = useParams<{ id: string }>();
  const [hostName, setHostName] = useState<string>("");
  const navigate = useNavigate();

  const handleHostEdit = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/hosts/${id}`);
      setHostName(response.data.host.name);
    } catch (error) {
      console.log(error);
    }
  }

  const handleFormSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await axios.patch(`http://localhost:8000/hosts/${id}`, { name: hostName });
      navigate(`/${id}`);
      console.log(response.data.message);  
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    handleHostEdit();
  }, [id]);

  return (
    <div className="container mt-5">
      <h1>Edit Host</h1>
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
          Update
        </button>
      </form>
    </div>
  );
};

export default EditHost;
