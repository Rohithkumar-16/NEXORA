import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Profile.css";

function Profile() {
  const navigate = useNavigate();
  const [profile, setProfile] = useState({
    name: "",
    college: "",
    studies: "",
    year: "",
    experience: "",
    skills: [],
    customSkill: "",
    interests: [],
    customInterest: "",
    goals: "",
    lookingFor: "",
    linkedin: "",
    linkedinProof: null,
    github: "",
    codeforces: "",
    achievement: "",
  });

  const skillOptions = [
    "Python",
    "C / C++",
    "Java",
    "JavaScript",
    "React",
    "SQL",
    "AI / ML",
    "Data Science",
  ];

  const interestOptions = [
    "Artificial Intelligence",
    "Data Science",
    "Web Development",
    "App Development",
    "Software Development",
    "Cybersecurity",
  ];

  const handleInputChange = (event) => {
    const { name, value } = event.target;

    setProfile((previous) => ({
      ...previous,
      [name]: value,
    }));
  };

  const toggleSelection = (field, value) => {
    setProfile((previous) => ({
      ...previous,
      [field]: previous[field].includes(value)
        ? previous[field].filter((item) => item !== value)
        : [...previous[field], value],
    }));
  };

  const completionItems = [
    profile.name,
    profile.college,
    profile.studies,
    profile.year,
    profile.experience,
    profile.skills.length > 0,
    profile.interests.length > 0,
    profile.goals,
    profile.lookingFor,
  ];

  const completedItems = completionItems.filter(Boolean).length;

  const profileCompletion = Math.round(
    (completedItems / completionItems.length) * 100,
  );
  const handleSubmit = (event) => {
    event.preventDefault();

    console.log("NEXORA PROFILE:", profile);

    // Save profile in browser storage
    localStorage.setItem("nexoraProfile", JSON.stringify(profile));

    alert("Your NEXORA profile has been created!");

    navigate("/profile-preview");
  };

  return (
    <div className="profile-page">
      {/* NAVIGATION */}

      <nav className="profile-navbar">
        <a href="/" className="profile-logo">
          NEXORA<span></span>
        </a>

        <a href="/" className="profile-back">
          ← Back to NEXORA
        </a>
      </nav>

      {/* PAGE INTRODUCTION */}

      <header className="profile-header">
        <div className="profile-badge">NEXORA • STUDENT PROFILE</div>

        <h1>
          Build your
          <span> profile.</span>
        </h1>

        <p>
          Tell NEXORA about your skills, interests, experience and goals. Your
          profile will help us connect you with relevant projects and potential
          teammates.
        </p>
      </header>

      {/* PROFILE FORM */}

      <main className="profile-container">
        <div className="profile-completion">
          <div className="completion-header">
            <div>
              <span>PROFILE COMPLETION</span>
              <strong>{profileCompletion}%</strong>
            </div>

            <p>
              {profileCompletion === 100
                ? "Your profile is ready!"
                : "Complete your profile to get better matches."}
            </p>
          </div>

          <div className="completion-bar">
            <div
              className="completion-progress"
              style={{ width: `${profileCompletion}%` }}
            />
          </div>
        </div>
        <form onSubmit={handleSubmit}>
          {/* 01 — STUDIES & EXPERIENCE */}
          {/* 01 — BACKGROUND */}

          <section className="profile-section">
            <div className="profile-step">01</div>

            <div className="profile-section-content">
              <h2>Your Background</h2>

              <p>Tell us about your current education and experience.</p>

              <div className="profile-fields">
                {/* FULL NAME */}
                <div className="profile-field">
                  <label htmlFor="name">Full Name</label>

                  <input
                    id="name"
                    type="text"
                    name="name"
                    value={profile.name}
                    onChange={handleInputChange}
                    placeholder="Enter your full name"
                    required
                  />
                </div>

                {/* COLLEGE */}
                <div className="profile-field">
                  <label htmlFor="college">College / University</label>

                  <input
                    id="college"
                    type="text"
                    name="college"
                    value={profile.college}
                    onChange={handleInputChange}
                    placeholder="Example: Marwadi University"
                    required
                  />
                </div>

                {/* COURSE */}
                <div className="profile-field">
                  <label htmlFor="studies">Course / Branch</label>

                  <input
                    id="studies"
                    type="text"
                    name="studies"
                    value={profile.studies}
                    onChange={handleInputChange}
                    placeholder="Example: B.Tech CSE AI & DS"
                    required
                  />
                </div>

                {/* YEAR */}
                <div className="profile-field">
                  <label htmlFor="year">Year of Study</label>

                  <select
                    id="year"
                    name="year"
                    value={profile.year}
                    onChange={handleInputChange}
                    required
                  >
                    <option value="">Select your year</option>
                    <option value="1st Year">1st Year</option>
                    <option value="2nd Year">2nd Year</option>
                    <option value="3rd Year">3rd Year</option>
                    <option value="4th Year">4th Year</option>
                  </select>
                </div>
              </div>

              {/* EXPERIENCE */}

              <div className="profile-field">
                <label htmlFor="experience">Experience Level</label>

                <select
                  id="experience"
                  name="experience"
                  value={profile.experience}
                  onChange={handleInputChange}
                  required
                >
                  <option value="">Select experience level</option>
                  <option value="Beginner">Beginner</option>
                  <option value="Intermediate">Intermediate</option>
                  <option value="Advanced">Advanced</option>
                </select>
              </div>
            </div>
          </section>

          {/* 02 — SKILLS */}

          <section className="profile-section">
            <div className="profile-step">02</div>

            <div className="profile-section-content">
              <h2>Your Skills</h2>

              <p>Select the technical skills you currently have.</p>

              <div className="profile-options">
                {skillOptions.map((skill) => (
                  <button
                    key={skill}
                    type="button"
                    className={
                      profile.skills.includes(skill)
                        ? "profile-option selected"
                        : "profile-option"
                    }
                    onClick={() => toggleSelection("skills", skill)}
                  >
                    <span className="option-check">
                      {profile.skills.includes(skill) ? "✓" : "+"}
                    </span>

                    {skill}
                  </button>
                ))}
              </div>
            </div>
          </section>

          {/* 03 — INTERESTS */}

          <section className="profile-section">
            <div className="profile-step">03</div>

            <div className="profile-section-content">
              <h2>Your Interests</h2>

              <p>Choose the areas of technology you are interested in.</p>

              <div className="profile-options">
                {interestOptions.map((interest) => (
                  <button
                    key={interest}
                    type="button"
                    className={
                      profile.interests?.includes(interest)
                        ? "profile-option selected"
                        : "profile-option"
                    }
                    onClick={() => toggleSelection("interests", interest)}
                  >
                    <span className="option-check">
                      {profile.interests?.includes(interest) ? "✓" : "+"}
                    </span>

                    {interest}
                  </button>
                ))}
              </div>
            </div>
          </section>

          {/* 04 — GOALS */}

          <section className="profile-section">
            <div className="profile-step">04</div>

            <div className="profile-section-content">
              <h2>Your Goals</h2>

              <p>Tell us what you want to achieve through NEXORA.</p>

              <textarea
                name="goals"
                value={profile.goals}
                onChange={handleInputChange}
                placeholder="Example: I want to gain experience by building real-world AI projects with other students."
                rows="5"
                required
              />
            </div>
          </section>

          {/* 05 — TEAMMATE / PROJECT PREFERENCE */}

          <section className="profile-section">
            <div className="profile-step">05</div>

            <div className="profile-section-content">
              <h2>What are you looking for?</h2>

              <p>
                Describe the type of project or teammates you want to
                collaborate with.
              </p>

              <textarea
                name="lookingFor"
                value={profile.lookingFor}
                onChange={handleInputChange}
                placeholder="Example: Looking for teammates interested in AI, Python and healthcare projects."
                rows="5"
                required
              />
            </div>
          </section>

          {/* 06 — PROFESSIONAL IDENTITY */}

          <section className="profile-section">
            <div className="profile-step">06</div>

            <div className="profile-section-content">
              <h2>Professional Identity</h2>

              <p>
                Adding your LinkedIn profile can help other students understand
                who you are and build trust. This section is completely
                optional.
              </p>

              <div className="profile-field">
                <label htmlFor="linkedin">
                  LinkedIn Profile{" "}
                  <span className="required-label">REQUIRED</span>
                </label>

                <div className="linkedin-input-row">
                  <input
                    id="linkedin"
                    type="url"
                    name="linkedin"
                    value={profile.linkedin || ""}
                    onChange={handleInputChange}
                    placeholder="https://www.linkedin.com/in/your-name"
                    required
                  />

                  {profile.linkedin && (
                    <a
                      href={profile.linkedin}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="linkedin-open"
                    >
                      Open ↗
                    </a>
                  )}
                </div>
              </div>

              <div className="identity-create">
                <div>
                  <strong>Don't have LinkedIn yet?</strong>
                  <p>
                    Your LinkedIn profile is required to create your NEXORA
                    profile. It helps establish a more trustworthy student
                    identity and allows teammates to understand your
                    professional background.
                  </p>
                </div>

                <a
                  href="https://www.linkedin.com/signup/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="create-account-button"
                >
                  Create LinkedIn Account ↗
                </a>
              </div>

              <div className="identity-proof">
                <div className="identity-proof-icon">✓</div>

                <div>
                  <strong>Why add LinkedIn?</strong>

                  <p>
                    A professional profile can help teammates understand your
                    background and make collaboration more trustworthy.
                  </p>
                </div>
              </div>
            </div>
          </section>

          {/* 07 — SKILL PROOF & ACHIEVEMENTS */}

          <section className="profile-section">
            <div className="profile-step">07</div>

            <div className="profile-section-content">
              <h2>Skill Proof & Achievements</h2>

              <p>
                Showcase your coding experience and achievements. A GitHub
                account is required to create your NEXORA profile and helps
                teammates understand your technical work.
              </p>

              {/* ================= GITHUB ================= */}

              <div className="proof-card">
                <div className="proof-card-header">
                  <div>
                    <strong>
                      GitHub <span className="required-star">*</span>
                    </strong>

                    <span>Projects & Open Source</span>
                  </div>

                  <div className="proof-status required-status">REQUIRED</div>
                </div>

                <input
                  type="text"
                  name="github"
                  value={profile.github || ""}
                  onChange={handleInputChange}
                  placeholder="Enter GitHub username"
                  required
                />

                <div className="proof-help">
                  <span>GitHub is required to continue.</span>

                  <a
                    href="https://github.com/signup"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    Create GitHub Account ↗
                  </a>
                </div>
              </div>

              {/* ================= CODEFORCES ================= */}

              <div className="proof-card">
                <div className="proof-card-header">
                  <div>
                    <strong>Codeforces</strong>

                    <span>Competitive Programming</span>
                  </div>

                  <div className="proof-status">OPTIONAL</div>
                </div>

                <input
                  type="text"
                  name="codeforces"
                  value={profile.codeforces || ""}
                  onChange={handleInputChange}
                  placeholder="Enter Codeforces handle"
                />

                <div className="proof-help">
                  <span>Don't have Codeforces yet? That's okay.</span>

                  <a
                    href="https://codeforces.com/register"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    Create Codeforces Account ↗
                  </a>
                </div>
              </div>

              {/* ================= OTHER ACHIEVEMENT ================= */}

              <div className="profile-field achievement-field">
                <label htmlFor="achievement">
                  Other Achievement{" "}
                  <span className="optional-label">OPTIONAL</span>
                </label>

                <input
                  id="achievement"
                  type="text"
                  name="achievement"
                  value={profile.achievement || ""}
                  onChange={handleInputChange}
                  placeholder="Example: Hackathon winner, AWS certificate, Chess rating..."
                />

                <small className="achievement-note">
                  No achievements yet? You can add them later.
                </small>
              </div>

              {/* ================= BEGINNER MESSAGE ================= */}

              <div className="skill-proof-note">
                <span>✦</span>

                <div>
                  <strong>Just getting started?</strong>

                  <p>
                    That's completely fine. You don't need Codeforces,
                    certificates or other achievements to create a NEXORA
                    profile. Start with your skills and interests, and add your
                    achievements as you grow.
                  </p>
                </div>
              </div>
            </div>
          </section>

          {/* SUBMIT */}

          <div className="profile-submit">
            <button type="submit">
              Create Profile
              <span>→</span>
            </button>
          </div>
        </form>
      </main>
    </div>
  );
}

export default Profile;
