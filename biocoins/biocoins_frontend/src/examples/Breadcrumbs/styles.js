// @mui material components
import { makeStyles } from "@mui/styles";

export default makeStyles(({ palette }) => ({
  breadcrumbs: {
    "& .MuiBreadcrumbs-separator": {
      color: ({ light }) => (light ? palette.white.main : palette.grey[600]),
    },
  },
}));
