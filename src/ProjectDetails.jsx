import { Link, useParams } from "react-router-dom";
import "./App.css";

const projects = {
  "ai-healthcare": {
    number: "01",
    icon: "🏥",
    title: "AI Healthcare Assistant",
    description:
      "An intelligent healthcare assistant designed to help users access useful healthcare information through AI-powered technology.",
    tags: ["AI / ML", "Python", "React"],
    goal: "Build a simple and accessible AI-powered platform that can provide users with useful healthcare information.",
    lookingFor: ["Python / AI Developer", "React Developer", "UI/UX Designer"],
  },

  "smart-agriculture": {
    number: "02",
    icon: "🌱",
    title: "Smart Agriculture",
    description:
      "A student project exploring technology-driven solutions for modern agriculture using IoT, Python and data.",
    tags: ["IoT", "Python", "Data"],
    goal: "Use technology and data to create smarter and more efficient agricultural solutions.",
    lookingFor: ["IoT Developer", "Python Developer", "Data Analyst"],
  },

  "student-security": {
    number: "03",
    icon: "🔐",
    title: "Student Security Platform",
    description:
      "A collaborative project focused on creating safer digital experiences and security tools for students.",
    tags: ["Cybersecurity", "Web", "JavaScript"],
    goal: "Develop a student-focused platform that promotes safer and more secure digital experiences.",
    lookingFor: [
      "Cybersecurity Student",
      "JavaScript Developer",
      "Backend Developer",
    ],
  },
};

function ProjectDetails() {
  const { projectId } = useParams();

  const project = projects[projectId];

  if (!project) {
    return (
      <div className="project-details-page">
        <div className="project-details-container">
          <p className="section-label">PROJECT NOT FOUND</p>

          <h1>Project doesn't exist.</h1>

          <Link to="/" className="primary-button">
            ← Back to NEXORA
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="project-details-page">
      {/* BACK BUTTON */}

      <Link to="/" className="project-back">
        ← Back to NEXORA
      </Link>

      {/* PROJECT HEADER */}

      <div className="project-details-container">
        <div className="project-details-header">
          <div className="project-details-icon">{project.icon}</div>

          <div>
            <p className="section-label">PROJECT {project.number}</p>

            <h1>{project.title}</h1>

            <p className="project-details-description">{project.description}</p>
          </div>
        </div>

        {/* TAGS */}

        <div className="project-details-tags">
          {project.tags.map((tag) => (
            <span key={tag}>{tag}</span>
          ))}
        </div>

        {/* PROJECT INFORMATION */}

        <div className="project-details-grid">
          <div className="project-info-card">
            <p className="section-label">PROJECT GOAL</p>

            <h2>What are we building?</h2>

            <p>{project.goal}</p>
          </div>

          <div className="project-info-card">
            <p className="section-label">LOOKING FOR</p>

            <h2>Teammates</h2>

            <ul>
              {project.lookingFor.map((role) => (
                <li key={role}>{role}</li>
              ))}
            </ul>
          </div>
        </div>

        {/* JOIN PROJECT */}

        <div className="project-join-card">
          <div>
            <p className="section-label">INTERESTED?</p>

            <h2>Want to work on this project?</h2>

            <p>
              Create your NEXORA profile and connect with students working on
              projects that match your skills.
            </p>
          </div>

          <Link to="/profile" className="primary-button">
            Create Your Profile →
          </Link>
        </div>
      </div>
    </div>
  );
}

export default ProjectDetails;
