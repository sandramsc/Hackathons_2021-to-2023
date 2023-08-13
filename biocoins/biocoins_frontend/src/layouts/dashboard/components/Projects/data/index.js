// @mui material components
import Tooltip from "@mui/material/Tooltip";

// Soft UI Dashboard React components
import SuiBox from "components/SuiBox";
import SuiTypography from "components/SuiTypography";
import SuiAvatar from "components/SuiAvatar";

// Custom styles for the Projects
import styles from "layouts/dashboard/components/Projects/styles";

// Images
import logoTrial1 from "assets/images/small-logos/preclinicalstage.png";
import logoTrial2 from "assets/images/small-logos/earlystage.png";
import logoTrial3 from "assets/images/small-logos/clinicalstage.png";
import team1 from "assets/images/team-1.jpg";
import team2 from "assets/images/team-2.jpg";
import team3 from "assets/images/team-3.jpg";
import team4 from "assets/images/team-4.jpg";

export default function data() {
  const classes = styles();

  const avatars = (members) =>
    members.map(([image, name]) => (
      <Tooltip key={name} title={name} placeholder="bottom">
        <SuiAvatar src={image} alt="name" size="xs" customClass={classes.projects_tableAvatar} />
      </Tooltip>
    ));

  return {
    columns: [
      { name: "researcher", align: "left" },
      { name: "members", align: "left" },
      { name: "funding", align: "center" },
      { name: "clinical_stage", align: "center" },
    ],

    rows: [
      {
        researcher: [logoTrial1, "Non-toxic Malaria Drug Evaluation Platform"],
        members: (
          <SuiBox display="flex" py={1}>
            {avatars([
              [team1, "Ryan Tompson"],
              [team2, "Romina Hadid"],
              [team3, "Alexander Smith"],
              [team4, "Jessica Doe"],
            ])}
          </SuiBox>
        ),
        funding: (
          <SuiTypography variant="caption" textColor="text" fontWeight="medium">
            $14,000
          </SuiTypography>
        ),
        clinical_stage: (
          <SuiBox width="8rem" textAlign="left">
            PRE-CLINICAL
          </SuiBox>
        ),
      },
      {
        researcher: [logoTrial2, "IntraClear Biologics B2HF"],
        members: (
          <SuiBox display="flex" py={1}>
            {avatars([
              [team2, "Romina Hadid"],
              [team4, "Jessica Doe"],
            ])}
          </SuiBox>
        ),
        funding: (
          <SuiTypography variant="caption" textColor="text" fontWeight="medium">
            $3,000
          </SuiTypography>
        ),
        clinical_stage: (
          <SuiBox width="8rem" textAlign="left">
            EARLY STAGE
          </SuiBox>
        ),
      },
      {
        researcher: [logoTrial3, "Heparanase Inhibitors for Cancer Therapeutics"],
        members: (
          <SuiBox display="flex" py={1}>
            {avatars([
              [team1, "Ryan Tompson"],
              [team3, "Alexander Smith"],
            ])}
          </SuiBox>
        ),
        funding: (
          <SuiTypography variant="caption" textColor="text" fontWeight="medium">
            Not set
          </SuiTypography>
        ),
        clinical_stage: (
          <SuiBox width="8rem" textAlign="left">
            CLINICAL TRIALS
          </SuiBox>
        ),
      },
      {
        researcher: [logoTrial2, "RNF167 as mTOR Targets"],
        members: (
          <SuiBox display="flex" py={1}>
            {avatars([
              [team4, "Jessica Doe"],
              [team3, "Alexander Smith"],
              [team2, "Romina Hadid"],
              [team1, "Ryan Tompson"],
            ])}
          </SuiBox>
        ),
        funding: (
          <SuiTypography variant="caption" textColor="text" fontWeight="medium">
            $20,500
          </SuiTypography>
        ),
        clinical_stage: (
          <SuiBox width="8rem" textAlign="left">
            EARLY STAGE
          </SuiBox>
        ),
      },
      {
        researcher: [logoTrial1, "Brain Cell Replacement Therapy "],
        members: (
          <SuiBox display="flex" py={1}>
            {avatars([[team4, "Jessica Doe"]])}
          </SuiBox>
        ),
        funding: (
          <SuiTypography variant="caption" textColor="text" fontWeight="medium">
            $500
          </SuiTypography>
        ),
        clinical_stage: (
          <SuiBox width="8rem" textAlign="left">
            PRE-CLINICAL
          </SuiBox>
        ),
      },
      {
        researcher: [logoTrial1, "Treatment of Neurological Conditions with Probiotics"],
        members: (
          <SuiBox display="flex" py={1}>
            {avatars([
              [team1, "Ryan Tompson"],
              [team4, "Jessica Doe"],
            ])}
          </SuiBox>
        ),
        funding: (
          <SuiTypography variant="caption" textColor="text" fontWeight="medium">
            $2,000
          </SuiTypography>
        ),
        clinical_stage: (
          <SuiBox width="8rem" textAlign="left">
            PRE-CLINICAL
          </SuiBox>
        ),
      },
    ],
  };
}
