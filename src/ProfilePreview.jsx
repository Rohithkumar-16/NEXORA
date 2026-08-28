import { Link } from "react-router-dom";
import "./ProfilePreview.css";

function ProfilePreview() {
  const savedProfile = localStorage.getItem("nexoraProfile");
  const profile = savedProfile ? JSON.parse(savedProfile) : null;

  if (!profile) {
    return (
      <div className="preview-page empty-preview">
        <div className="empty-card">
          <div className="empty-icon">!</div>

          <h1>Profile not found</h1>

          <p>
            You haven't created your NEXORA profile yet. Create one to get
            started.
          </p>

          <Link to="/profile" className="primary-button">
            Create Profile →
          </Link>
        </div>
      </div>
    );
  }

  const firstLetter = profile.name?.trim()?.charAt(0)?.toUpperCase() || "N";

  return (
    <div className="preview-page">
      {/* ================= NAVBAR ================= */}

      <nav className="preview-navbar">
        <Link to="/" className="preview-logo">
          NEXORA<span></span>
        </Link>

        <Link to="/profile" className="preview-back">
          ✏ Edit Profile
        </Link>
      </nav>

      {/* ================= WELCOME ================= */}

      <section className="welcome-section">
        <div className="welcome-content">
          <p className="welcome-label">YOUR NEXORA PROFILE</p>

          <h1>
            Hi, <span>{profile.name}</span>!!
          </h1>

          <p className="welcome-description">
            Your profile is ready. This is how other students in the NEXORA
            community can discover you.
          </p>
        </div>

        <div className="profile-status">
          <span className="status-dot"></span>
          Profile Created
        </div>
      </section>

      {/* ================= PROFILE CONTAINER ================= */}

      <main className="preview-container">
        <div className="profile-preview-card">
          {/* ================= PROFILE HEADER ================= */}

          <div className="profile-card-header">
            <div className="preview-avatar">
              <span>{firstLetter}</span>
            </div>

            <div className="profile-main-info">
              <h2>{profile.name}</h2>

              {profile.studies && <p>{profile.studies}</p>}

              {profile.college && (
                <span className="college-text">🎓 {profile.college}</span>
              )}

              {profile.year && (
                <span className="year-badge">{profile.year}</span>
              )}
            </div>
          </div>

          {/* ================= PROFILE CONTENT ================= */}

          <div className="profile-content">
            {/* EXPERIENCE */}

            {profile.experience && (
              <div className="preview-section">
                <div className="section-heading">
                  <span className="section-icon">💼</span>
                  <h3>Experience</h3>
                </div>

                <p>{profile.experience}</p>
              </div>
            )}

            {/* SKILLS */}

            {profile.skills?.length > 0 && (
              <div className="preview-section">
                <div className="section-heading">
                  <span className="section-icon">⚡</span>
                  <h3>Skills</h3>
                </div>

                <div className="preview-tags">
                  {profile.skills.map((skill, index) => (
                    <span key={`${skill}-${index}`} className="skill-tag">
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {/* INTERESTS */}

            {profile.interests?.length > 0 && (
              <div className="preview-section">
                <div className="section-heading">
                  <span className="section-icon">♡</span>
                  <h3>Interests</h3>
                </div>

                <div className="preview-tags">
                  {profile.interests.map((interest, index) => (
                    <span key={`${interest}-${index}`} className="interest-tag">
                      {interest}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {/* GOALS */}

            {profile.goals && (
              <div className="preview-section">
                <div className="section-heading">
                  <span className="section-icon">🎯</span>
                  <h3>Goals</h3>
                </div>

                <p>{profile.goals}</p>
              </div>
            )}

            {/* LOOKING FOR */}

            {profile.lookingFor && (
              <div className="preview-section">
                <div className="section-heading">
                  <span className="section-icon">🤝</span>
                  <h3>Looking For</h3>
                </div>

                <p>{profile.lookingFor}</p>
              </div>
            )}

            {/* PROFESSIONAL IDENTITY */}

            {(profile.linkedin || profile.github) && (
              <div className="preview-section">
                <div className="section-heading">
                  <span className="section-icon">🔗</span>
                  <h3>Professional Identity</h3>
                </div>

                <div className="preview-links">
                  {profile.linkedin && (
                    <a
                      href={profile.linkedin}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="professional-link linkedin-link"
                    >
                      <span>in</span>
                      LinkedIn
                      <strong>↗</strong>
                    </a>
                  )}

                  {profile.github && (
                    <a
                      href={
                        profile.github.startsWith("http")
                          ? profile.github
                          : `https://github.com/${profile.github}`
                      }
                      target="_blank"
                      rel="noopener noreferrer"
                      className="professional-link github-link"
                    >
                      <span>◉</span>
                      GitHub
                      <strong>↗</strong>
                    </a>
                  )}
                </div>
              </div>
            )}

            {/* ACHIEVEMENTS */}

            {(profile.codeforces || profile.achievement) && (
              <div className="preview-section">
                <div className="section-heading">
                  <span className="section-icon">🏆</span>
                  <h3>Achievements</h3>
                </div>

                <div className="achievement-list">
                  {profile.codeforces && (
                    <p>
                      <strong>Codeforces:</strong> {profile.codeforces}
                    </p>
                  )}

                  {profile.achievement && <p>{profile.achievement}</p>}
                </div>
              </div>
            )}
          </div>

          {/* ================= CARD FOOTER ================= */}

          <div className="profile-card-footer">
            <span>Built with</span>
            <strong>NEXORA.</strong>
            <span>• Connect. Collaborate. Grow.</span>
          </div>
        </div>

        {/* ================= ACTION BUTTONS ================= */}

        <div className="preview-actions">
          <Link to="/profile" className="secondary-button">
            ← Edit Profile
          </Link>

          <Link to="/" className="primary-button">
            Explore NEXORA →
          </Link>
        </div>
      </main>
    </div>
  );
}

export default ProfilePreview;
