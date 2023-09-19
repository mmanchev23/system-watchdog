import axios from "axios";
import Pagination from "../Shared/Pagination";
import { useEffect, useState, SyntheticEvent } from "react";
import { useParams, useNavigate } from "react-router-dom";

interface HostDetails {
  id: string;
  name: string;
}

interface CPUData {
  id: string;
  load: number;
}

interface RXPkt {
  id: string;
  packets: number;
}

const Host = () => {
  const { id } = useParams<{ id: string }>();
  const [HostDetails, setHostDetails] = useState<HostDetails>();
  const [cpuDataLength, setCPUDataLength] = useState<number>(0);
  const [packetsLength, setPacketsLength] = useState<number>(0);
  const [cpuData, setCPUData] = useState<CPUData[]>([]);
  const [rxPackets, setRXPackets] = useState<RXPkt[]>([]);
  const [cpuPage, setCpuPage] = useState<number>(1);
  const [packetPage, setPacketPage] = useState<number>(1);
  const navigate = useNavigate();

  const fetchHost = async () => {
    try {
      const response = await axios.get<{ host: HostDetails }>(`http://localhost:8000/hosts/${id}`);
      setHostDetails(response.data.host);
    } catch (error) {
      console.log(error);
    }
  }

  const fetchCPUData = async () => {
    try {
      const response = await axios.get<{ cpu_data: CPUData[], count: number }>(`http://localhost:8000/cpu-data/${id}?page=${cpuPage}`);
      setCPUData(response.data.cpu_data);
      setCPUDataLength(Math.ceil(response.data.count / 10));
    } catch (error) {
      console.log(error);
    }
  }

  const fetchPackets = async () => {
    try {
      const response = await axios.get<{ rxpkt: RXPkt[], count: number }>(`http://localhost:8000/rxpkt/${id}?page=${packetPage}`);
      setRXPackets(response.data.rxpkt);
      setPacketsLength(Math.ceil(response.data.count / 10));
    } catch (error) {
      console.log(error);
    }
  }

  const handleHostDataRetrieval = async (e: SyntheticEvent) => {
    e.preventDefault();

    try {
      const response = await await axios.post(`http://localhost:8000/metrics/`, {
        "host_id": id,
        "time": 10
      });

      window.location.reload();
      console.log(response.data.message);
    } catch (error) {
      console.log(error);
    }
  };

  const handleHostDelete = async (e: SyntheticEvent) => {
    e.preventDefault();

    try {
      const response = await axios.delete(`http://0.0.0.0:8000/hosts/${id}`);
      navigate("/");
      console.log(response.data.message);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchHost();
    fetchCPUData();
    fetchPackets();
  }, [id, cpuPage, packetPage]);

  return (
    <div className="container mt-5">
      <h1 className="d-flex justify-content-between align-items-center mb-4">
        {HostDetails?.name}
        <div className="d-flex gap-2">
          <button
            className="btn btn-warning mr-3 w-50"
            onClick={handleHostDataRetrieval}
          >
            <i className="fa fa-database" aria-hidden="true"></i>
          </button>
          <button
            className="btn btn-primary mr-3 w-50"
            onClick={() => navigate(`/${id}/edit`)}
          >
            <i className="fa fa-cogs" aria-hidden="true"></i>
          </button>
          <button
            className="btn btn-danger mr-3 w-50"
            onClick={handleHostDelete}
          >
            <i className="fa fa-trash" aria-hidden="true"></i>
          </button>
        </div>
      </h1>
      <div className="row">
        <div className="col-md-6">
          <div className="card">
            <div className="card-header">
              <h2>CPU</h2>
            </div>
            <ul className="list-group list-group-flush">
              {cpuData ? cpuData.map((cpu) => (
                <li key={cpu.id} className="list-group-item">
                  {cpu.load} %
                </li>
              )) : (
                <li className="list-group-item">
                  No CPU data available at the moment ...
                </li>
              )}
            </ul>
          </div>
          <br />
          {cpuData && cpuDataLength > 1 && <Pagination paginationLength={cpuDataLength} currentPage={cpuPage} onPageChange={setCpuPage} />}
        </div>

        <div className="col-md-6">
          <div className="card">
            <div className="card-header">
              <h2>Packets</h2>
            </div>
            <ul className="list-group list-group-flush">
              {rxPackets ? rxPackets.map((packet) => (
                <li key={packet.id} className="list-group-item">
                  {packet.packets}
                </li>
              )) : (
                <li className="list-group-item">
                  No Packet data available at the moment ...
                </li>
              )}
            </ul>
          </div>
          <br />
          {rxPackets && packetsLength > 1 && <Pagination paginationLength={packetsLength} currentPage={packetPage} onPageChange={setPacketPage} />}
        </div>
      </div>
    </div>
  );
};

export default Host;
