import { useState } from "react";

// @mui material components
import Card from "@mui/material/Card";
import Icon from "@mui/material/Icon";
import Menu from "@mui/material/Menu";
import MenuItem from "@mui/material/MenuItem";

// Soft UI Dashboard React components
import SuiBox from "components/SuiBox";
import SuiTypography from "components/SuiTypography";

// Soft UI Dashboard Materail-UI example components
import Table from "examples/Table";

// Custom styles for the Projects
import styles from "layouts/dashboard/components/Projects/styles";

// Data
import data from "layouts/dashboard/components/Projects/data";

function Projects() {
  const { columns, rows } = data();
  const [menu, setMenu] = useState(null);
  const classes = styles();

  const openMenu = ({ currentTarget }) => setMenu(currentTarget);
  const closeMenu = () => setMenu(null);

  const renderMenu = (
    <Menu
      id="simple-menu"
      anchorEl={menu}
      anchorOrigin={{
        vertical: "top",
        horizontal: "left",
      }}
      transformOrigin={{
        vertical: "top",
        horizontal: "right",
      }}
      open={Boolean(menu)}
      onClose={closeMenu}
    >
      <MenuItem onClick={closeMenu}>Action</MenuItem>
      <MenuItem onClick={closeMenu}>Another action</MenuItem>
      <MenuItem onClick={closeMenu}>Something else</MenuItem>
    </Menu>
  );

  return (
    <Card>
      <SuiBox display="flex" justifyContent="space-between" alignItems="center" p={3}>
        <SuiBox>
          <SuiTypography variant="h6" gutterBottom>
            Clinical Trials
          </SuiTypography>
          <SuiBox display="flex" alignItems="center" lineHeight={0}>
            <Icon className="font-bold text-info">done</Icon>
            <SuiTypography variant="button" fontWeight="regular" textColor="text">
              &nbsp;<strong>30 added</strong> this month
            </SuiTypography>
          </SuiBox>
        </SuiBox>
        <SuiBox color="text" px={2}>
          <Icon className="cursor-pointer font-bold" fontSize="small" onClick={openMenu}>
            more_vert
          </Icon>
        </SuiBox>
        {renderMenu}
      </SuiBox>
      <SuiBox customClass={classes.projects_table}>
        <Table columns={columns} rows={rows} />
      </SuiBox>
    </Card>
  );
}

export default Projects;
