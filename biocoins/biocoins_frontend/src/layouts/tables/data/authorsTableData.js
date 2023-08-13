/* eslint-disable react/prop-types */
// Soft UI Dashboard React components
import SuiBox from "components/SuiBox";
import SuiTypography from "components/SuiTypography";
import SuiAvatar from "components/SuiAvatar";
import SuiBadge from "components/SuiBadge";

// Images
import team6 from "assets/images/team-6.jpg";
import team7 from "assets/images/team-7.jpg";
import team8 from "assets/images/team-8.jpg";
import team9 from "assets/images/team-9.jpg";
import team10 from "assets/images/team-10.jpg";
import team11 from "assets/images/team-11.jpg";
import team12 from "assets/images/team-12.jpg";

function Author({ image, name, email }) {
  return (
    <SuiBox display="flex" alignItems="center" px={1} py={0.5}>
      <SuiBox mr={2}>
        <SuiAvatar src={image} alt={name} size="sm" variant="rounded" />
      </SuiBox>
      <SuiBox display="flex" flexDirection="column">
        <SuiTypography variant="button" fontWeight="medium">
          {name}
        </SuiTypography>
        <SuiTypography variant="caption" textColor="secondary">
          {email}
        </SuiTypography>
      </SuiBox>
    </SuiBox>
  );
}

function Function({ job, org }) {
  return (
    <SuiBox display="flex" flexDirection="column">
      <SuiTypography variant="caption" fontWeight="medium" textColor="text">
        {job}
      </SuiTypography>
      <SuiTypography variant="caption" textColor="secondary">
        {org}
      </SuiTypography>
    </SuiBox>
  );
}

export default {
  columns: [
    { name: "team", align: "left" },
    { name: "function", align: "left" },
    { name: "status", align: "center" },
  ],

  rows: [
    {
      team: <Author image={team6} name="Sandra Ashipala" email="sandra@biocoins.com" />,
      function: <Function job="Computer Scientist" org="Developer" />,
      status: (
        <SuiBadge variant="gradient" badgeContent="online" color="success" size="extra-small" />
      ),
    },
    {
      team: <Author image={team7} name="Jason Mercurio" email="jason@biocoins.com" />,
      function: <Function job="Quantitative Analyst II" org="Analyst" />,
      status: (
        <SuiBadge variant="gradient" badgeContent="offline" color="secondary" size="extra-small" />
      ),
    },
    {
      team: <Author image={team8} name="Triyaksh Mathur" email="triyaksh@biocoins.com" />,
      function: <Function job="XR intern" org="Mixed Reality" />,
      status: (
        <SuiBadge variant="gradient" badgeContent="online" color="success" size="extra-small" />
      ),
    },
    {
      team: <Author image={team9} name="Ketan Bansal" email="ketan@biocoins.com" />,
      function: <Function job="Director of Machine Learing" org="Machine Learing" />,
      status: (
        <SuiBadge variant="gradient" badgeContent="online" color="success" size="extra-small" />
      ),
    },
    {
      team: <Author image={team10} name="Stephen Price" email="stephen@biocoins.com" />,
      function: <Function job="Chief Data Officer" org="Data Science" />,
      status: (
        <SuiBadge variant="gradient" badgeContent="offline" color="secondary" size="extra-small" />
      ),
    },
    {
      team: <Author image={team11} name="Aditiy Iyer" email="aditiy@biocoins.com" />,
      function: <Function job="Biomedical Engineering student" org="Biomedical Engineering" />,
      status: (
        <SuiBadge variant="gradient" badgeContent="offline" color="secondary" size="extra-small" />
      ),
    },
    {
      team: <Author image={team12} name="Chris Lovejoy" email="chris@biocoins.com" />,
      function: <Function job="NHS Medical Doctor" org="Medical Doctor" />,
      status: (
        <SuiBadge variant="gradient" badgeContent="offline" color="secondary" size="extra-small" />
      ),
    },
  ],
};
