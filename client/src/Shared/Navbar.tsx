import { Link } from "react-router-dom";
import { Navbar, Nav } from "react-bootstrap";

const Navigation = () => {
    return (
    <Navbar bg="light" expand="lg">
        <div className="container">
            <Navbar.Brand as={Link} to="/">
                Hosts
            </Navbar.Brand>
            <Navbar.Collapse id="navbarNav">
                <Nav className="mr-auto">
                <Nav.Link as={Link} to="/create">
                    Register Host
                </Nav.Link>
                <Nav.Link href="http://localhost:8080" target="_blank">
                    Admin Panel
                </Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </div>
    </Navbar>
    );
}

export default Navigation;