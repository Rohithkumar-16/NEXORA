import { Link } from "react-router-dom";
import "./ProfilePreview.css";

function ProfilePreview() {
  const savedProfile = localStorage.getItem("nexoraProfile");

  const profile = savedProfile ? JSON.parse(savedProfile) : null;

  if (!profile) {
    return (
      <div className="preview-page">
        <h1>Profile not found</h1>

        <Link to="/profile">Create Profile</Link>
      </div>
    );
  }

  return (
    <div className="preview-page">
      {/* NAVBAR */}

      <nav className="preview-navbar">
        <Link to="/" className="preview-logo">
          NEXORA<span>.</span>
        </Link>

        <Link to="/profile" className="preview-back">
          ← Edit Profile
        </Link>
      </nav>

      {/* HEADER */}

      <header className="preview-header">
        <div className="profile-badge">NEXORA • PROFILE CREATED</div>

        <h1>
          Your profile is
          <span> ready.</span>
        </h1>

        <p>Here's how other students will see your NEXORA profile.</p>
      </header>

      {/* PROFILE */}

      <main className="preview-container">
        <div className="profile-preview-card">
          {/* BASIC INFORMATION */}

          <div className="preview-top">
            <div className="preview-avatar">
              {profile.name?.charAt(0).toUpperCase()}
            </div>

            <div>
              <h2>{profile.name}</h2>

              <p>{profile.studies}</p>

              <span>{profile.college}</span>

              <small>{profile.year}</small>
            </div>
          </div>

          {/* EXPERIENCE */}

          <div className="preview-section">
            <h3>Experience</h3>

            <p>{profile.experience}</p>
          </div>

          {/* SKILLS */}

          <div className="preview-section">
            <h3>Skills</h3>

            <div className="preview-tags">
              {profile.skills?.map((skill) => (
                <span key={skill}>{skill}</span>
              ))}
            </div>
          </div>

          {/* INTERESTS */}

          <div className="preview-section">
            <h3>Interests</h3>

            <div className="preview-tags">
              {profile.interests?.map((interest) => (
                <span key={interest}>{interest}</span>
              ))}
            </div>
          </div>

          {/* GOALS */}

          <div className="preview-section">
            <h3>Goals</h3>

            <p>{profile.goals}</p>
          </div>

          {/* LOOKING FOR */}

          <div className="preview-section">
            <h3>Looking For</h3>

            <p>{profile.lookingFor}</p>
          </div>

          {/* PROFESSIONAL IDENTITY */}

          <div className="preview-section">
            <h3>Professional Identity</h3>

            <div className="preview-links">
              {profile.linkedin && (
                <a
                  href={profile.linkedin}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  LinkedIn ↗
                </a>
              )}

              {profile.github && (
                <a
                  href={`https://github.com/${profile.github}`}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  GitHub ↗
                </a>
              )}
            </div>
          </div>

          {/* ACHIEVEMENTS */}

          {(profile.codeforces || profile.achievement) && (
            <div className="preview-section">
              <h3>Achievements</h3>

              {profile.codeforces && <p>Codeforces: {profile.codeforces}</p>}

              {profile.achievement && <p>{profile.achievement}</p>}
            </div>
          )}
        </div>

        {/* ACTION BUTTONS */}

        <div className="preview-actions">
          <Link to="/profile" className="secondary-button">
            ← Edit Profile
          </Link>

          <Link to="/" className="primary-button">
            Go to NEXORA →
          </Link>
        </div>
      </main>
    </div>
  );
}

export default ProfilePreview;
