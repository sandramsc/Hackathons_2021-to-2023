// @mui material components
import Divider from "@mui/material/Divider";

// Soft UI Dashboard React components
import SuiBox from "components/SuiBox";
import SuiTypography from "components/SuiTypography";

function Separator() {
  return (
    <SuiBox position="relative" py={0.25}>
      <Divider />
      <SuiBox
        backgroundColor="white"
        position="absolute"
        top="50%"
        left="50%"
        px={1.5}
        style={{ transform: "translate(-50%, -60%)" }}
      >
        <SuiTypography variant="button" fontWeight="medium" textColor="secondary">
          or
        </SuiTypography>
      </SuiBox>
    </SuiBox>
  );
}

export default Separator;
