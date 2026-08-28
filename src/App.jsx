import { useState } from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import "./App.css";
import Profile from "./Profile";
import Login from "./Login";
import Signup from "./Signup";
import ProfilePreview from "./ProfilePreview";

function Home() {
  const [menuOpen, setMenuOpen] = useState(false);
  return (
    <div className="app">
      {/* ================= NAVBAR ================= */}
      <nav className="navbar">
        {/* LOGO */}
        <Link to="/" className="logo">
          NEXORA<span></span>
        </Link>

        {/* MAIN NAVIGATION */}
        <div className={`nav-links ${menuOpen ? "active" : ""}`}>
          <a href="#home" onClick={() => setMenuOpen(false)}>
            Home
          </a>

          <a href="#workflow" onClick={() => setMenuOpen(false)}>
            How It Works
          </a>

          <a href="#projects" onClick={() => setMenuOpen(false)}>
            Projects
          </a>

          <a href="#matching" onClick={() => setMenuOpen(false)}>
            AI Matching
          </a>

          <a href="#about" onClick={() => setMenuOpen(false)}>
            About
          </a>
        </div>

        {/* AUTH + WHATSAPP */}
        <div className="nav-auth">
          <a href="#" className="nav-whatsapp">
            WhatsApp
          </a>

          <Link to="/login" className="nav-login">
            Login
          </Link>

          <Link to="/signup" className="nav-button">
            Sign Up →
          </Link>
        </div>

        {/* MOBILE MENU */}
        <button className="menu-button" onClick={() => setMenuOpen(!menuOpen)}>
          ☰
        </button>
      </nav>

      {/* ================= HERO ================= */}

      <section className="hero-section" id="home">
        <div className="hero-glow"></div>

        <div className="hero-content">
          <p className="section-label">AI-POWERED STUDENT COLLABORATION</p>

          <h1>
            Find your people.
            <br />
            <span>Build something meaningful.</span>
          </h1>

          <p className="hero-description">
            NEXORA connects students with the right teammates and real-world
            projects using AI-powered team matching.
          </p>

          <div className="hero-buttons">
            <Link to="/profile" className="primary-button">
              Create Your Profile →
            </Link>

            <a href="#projects" className="secondary-button">
              Discover Projects
            </a>
          </div>
        </div>
      </section>

      {/* ================= HOW IT WORKS ================= */}

      <section className="workflow-section" id="workflow">
        <div className="section-heading">
          <p className="section-label">HOW NEXORA WORKS</p>

          <h2>
            From <span>profile</span> to project.
          </h2>

          <p className="section-description">
            NEXORA helps students move from finding teammates to building
            meaningful projects together.
          </p>
        </div>

        <div className="workflow-grid">
          <div className="workflow-card">
            <span>01</span>

            <div className="workflow-icon">👤</div>

            <h3>Create Profile</h3>

            <p>Add your studies, skills, interests, experience and goals.</p>
          </div>

          <div className="workflow-card">
            <span>02</span>

            <div className="workflow-icon">💡</div>

            <h3>Create or Discover</h3>

            <p>
              Create a project or discover projects that match your interests.
            </p>
          </div>

          <div className="workflow-card">
            <span>03</span>

            <div className="workflow-icon">🤖</div>

            <h3>AI Matching</h3>

            <p>
              NEXORA analyzes skills and project requirements to find potential
              teammates.
            </p>
          </div>

          <div className="workflow-card">
            <span>04</span>

            <div className="workflow-icon">🤝</div>

            <h3>Collaborate</h3>

            <p>Send collaboration requests and form your project team.</p>
          </div>

          <div className="workflow-card">
            <span>05</span>

            <div className="workflow-icon">🚀</div>

            <h3>Build Together</h3>

            <p>
              Work inside a shared project workspace and track your progress.
            </p>
          </div>
        </div>
      </section>

      {/* ================= PROJECT DISCOVERY ================= */}

      <section className="projects-section" id="projects">
        <div className="section-heading">
          <p className="section-label">DISCOVER PROJECTS</p>

          <h2>
            Ideas looking for
            <span> the right team.</span>
          </h2>

          <p className="section-description">
            Explore student projects and find opportunities where your skills
            can make an impact.
          </p>
        </div>

        <div className="projects-grid">
          <div className="project-card">
            <div className="project-number">01</div>

            <div className="project-icon">🏥</div>

            <h3>AI Healthcare Assistant</h3>

            <p>
              Building an intelligent healthcare assistant designed to help
              users access useful information.
            </p>

            <div className="project-tags">
              <span>AI / ML</span>
              <span>Python</span>
              <span>React</span>
            </div>

            <button>View Project →</button>
          </div>

          <div className="project-card">
            <div className="project-number">02</div>

            <div className="project-icon">🌱</div>

            <h3>Smart Agriculture</h3>

            <p>
              A student project exploring technology-driven solutions for modern
              agriculture.
            </p>

            <div className="project-tags">
              <span>IoT</span>
              <span>Python</span>
              <span>Data</span>
            </div>

            <button>View Project →</button>
          </div>

          <div className="project-card">
            <div className="project-number">03</div>

            <div className="project-icon">🔐</div>

            <h3>Student Security Platform</h3>

            <p>
              A collaborative project focused on creating safer digital
              experiences for students.
            </p>

            <div className="project-tags">
              <span>Cybersecurity</span>
              <span>Web</span>
              <span>JavaScript</span>
            </div>

            <button>View Project →</button>
          </div>
        </div>
      </section>

      {/* ================= AI MATCHING ================= */}

      <section className="matching-section" id="matching">
        <div className="matching-content">
          <div>
            <p className="section-label">AI TEAM MATCHING</p>

            <h2>
              Stop searching.
              <br />
              Let AI find your
              <span> perfect team.</span>
            </h2>

            <p className="matching-description">
              NEXORA analyzes student profiles and project requirements to
              generate ranked teammate recommendations with match scores and
              explanations.
            </p>

            <Link to="/profile" className="primary-button">
              Build Your Profile →
            </Link>
          </div>

          <div className="match-card">
            <div className="match-header">
              <div>
                <small>AI MATCH</small>

                <h3>Recommended Teammate</h3>
              </div>

              <div className="match-score">94%</div>
            </div>

            <div className="match-person">
              <div className="avatar">A</div>

              <div>
                <strong>Student Profile</strong>

                <p>AI • Python • Data Science</p>
              </div>
            </div>

            <div className="match-skills">
              <span>Python ✓</span>

              <span>Machine Learning ✓</span>

              <span>Data Science ✓</span>
            </div>

            <div className="match-reason">
              <small>WHY THIS MATCH?</small>

              <p>
                Strong skill overlap with your project's technical requirements
                and interests.
              </p>
            </div>

            <button className="match-button">
              Send Collaboration Request →
            </button>
          </div>
        </div>
      </section>

      {/* ================= COLLABORATION ================= */}

      <section className="collaboration-section">
        <div className="section-heading">
          <p className="section-label">COLLABORATE</p>

          <h2>
            Build the team.
            <span> Build the project.</span>
          </h2>

          <p className="section-description">
            Connect with students whose skills complement your own and turn
            ideas into working projects.
          </p>
        </div>

        <div className="team-flow">
          <div className="team-person">
            <div className="team-avatar">K</div>

            <h3>You</h3>

            <p>AI • Python</p>
          </div>

          <div className="team-line">
            <span>Collaboration Request</span>
            <div></div>
          </div>

          <div className="team-person">
            <div className="team-avatar">R</div>

            <h3>Teammate</h3>

            <p>React • UI/UX</p>
          </div>

          <div className="team-line">
            <span>Build Together</span>
            <div></div>
          </div>

          <div className="team-person">
            <div className="team-avatar">S</div>

            <h3>Teammate</h3>

            <p>Backend • SQL</p>
          </div>
        </div>
      </section>

      {/* ================= WORKSPACE ================= */}

      <section className="workspace-section">
        <div className="workspace-content">
          <div>
            <p className="section-label">PROJECT WORKSPACE</p>

            <h2>
              Everything your team needs
              <span> in one place.</span>
            </h2>

            <p>
              Once your team is formed, manage tasks, milestones, discussions,
              resources and project progress through a shared workspace.
            </p>
          </div>

          <div className="workspace-card">
            <div className="workspace-top">
              <div>
                <small>PROJECT</small>

                <h3>AI Healthcare Assistant</h3>
              </div>

              <span>68%</span>
            </div>

            <div className="workspace-progress">
              <div></div>
            </div>

            <div className="workspace-stats">
              <div>
                <strong>12</strong>

                <small>Tasks</small>
              </div>

              <div>
                <strong>3</strong>

                <small>Milestones</small>
              </div>

              <div>
                <strong>24</strong>

                <small>Discussions</small>
              </div>

              <div>
                <strong>8</strong>

                <small>Resources</small>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ================= ABOUT ================= */}

      <section className="about-section" id="about">
        <div className="about-content">
          <p className="section-label">ABOUT NEXORA</p>

          <h2>
            Turning student ideas
            <span> into real projects.</span>
          </h2>

          <p className="about-text">
            NEXORA is an AI-powered student project collaboration platform
            designed to help students discover projects, find compatible
            teammates and build together.
          </p>

          <p className="about-text">
            The platform combines student profiles, project requirements and
            AI-based matching to make project collaboration easier and more
            meaningful.
          </p>
        </div>
      </section>

      {/* ================= FINAL CTA ================= */}

      <section className="cta-section">
        <p className="section-label">START BUILDING</p>

        <h2>
          Your next project
          <span> starts here.</span>
        </h2>

        <p>
          Create your profile and let NEXORA help you find the right project and
          teammates.
        </p>

        <Link to="/profile" className="primary-button">
          Create Your Profile →
        </Link>
      </section>

      {/* ================= FOOTER ================= */}

      <footer className="footer">
        <div className="footer-logo">
          NEXORA<span></span>
        </div>

        <p>AI-powered student project collaboration.</p>

        <div className="footer-links">
          <a href="#home">Home</a>

          <a href="#workflow">How It Works</a>

          <a href="#projects">Projects</a>

          <a href="#matching">AI Matching</a>

          <Link to="/profile">Profile</Link>
        </div>

        <p className="copyright">© 2026 NEXORA. All rights reserved.</p>
      </footer>
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/profile-preview" element={<ProfilePreview />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
