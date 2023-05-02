import { createGlobalStyle } from 'styled-components';

/* istanbul ignore next */
export const GlobalStyle = createGlobalStyle`
  body {
    margin: 0;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", "Noto Sans", "Liberation Sans", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  *, ::after, ::before {
    box-sizing: border-box;
  }

  div {
    display: block;
  }

  p {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    width: 100%;
  }

  a, a:hover {
    text-decoration: none;
    font-family: "Cerebri Sans", sans-serif;
    color: #00477d;
  }

  td a:hover {
    color: #000;
    text-decoration: underline;
  }

  code {
    font-family: Consolas, source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;

  }

  .link-body-emphasis {
    font-weight: normal;
    color: #5e5e5e;
    text-decoration: none;
  }

  .link-body-emphasis:hover {
    color: #3F4254;
  }

  .link-table {
    color: #3b506c;
    font-weight: normal;
    text-decoration: none;
  }

  .breadcrumb-chevron {
    --bs-breadcrumb-divider: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='%236c757d'%3E%3Cpath fill-rule='evenodd' d='M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z'/%3E%3C/svg%3E");
    gap: .5rem;
  }

  .breadcrumb-item + .breadcrumb-item::before {
    float: left;
    padding-right: var(--bs-breadcrumb-item-padding-x);
    color: var(--bs-breadcrumb-divider-color);
    content: var(--bs-breadcrumb-divider, "/");
  }

  .rounded-3 {
    border-radius: 0.5rem !important;
  }

  .bg-body-tertiary {
    --bs-bg-opacity: 1;
    background-color: rgba(248, 249, 250, 1) !important;
  }

  .p-3 {
    padding: 1rem !important;
  }

  .fw-semibold {
    font-weight: 600 !important;
  }

  .breadcrumb {
    --bs-breadcrumb-padding-x: 0;
    --bs-breadcrumb-padding-y: 0;
    --bs-breadcrumb-margin-bottom: 1rem;
    --bs-breadcrumb-bg: #ffffff;
    --bs-breadcrumb-border-radius: 0.5rem;
    --bs-breadcrumb-divider-color: rgba(33, 37, 41, 0.75);
    --bs-breadcrumb-item-padding-x: 0.5rem;
    --bs-breadcrumb-item-active-color: rgba(33, 37, 41, 0.75);
    display: flex;
    flex-wrap: wrap;
    padding: var(--bs-breadcrumb-padding-y) var(--bs-breadcrumb-padding-x);
    margin-bottom: var(--bs-breadcrumb-margin-bottom);
    line-height: 0.9em;
    list-style: none;
    background-color: var(--bs-breadcrumb-bg);
    border-radius: var(--bs-breadcrumb-border-radius);
  }

  dl, ol, ul {
    margin-top: 0;
    margin-bottom: 1rem;
  }

  .list-group {
    width: 100%;
    max-width: fit-content;
    border-radius: 0.375rem;
  }

  .list-group-item {
    position: relative;
    display: block;
    padding: 0.5rem 1rem;
    color: #212529;
    text-decoration: none;
    background-color: #ffffff;
    min-width: fit-content;
  }

  .list-group-item + .list-group-item {
    border-top-width: 0;
  }

  .list-group-item:first-child {
    border-top-left-radius: inherit;
    border-top-right-radius: inherit;
  }

  .d-flex {
    display: flex !important;
  }

  .gap-2 {
    gap: .5rem !important;
  }

  .justify-content-between {
    justify-content: space-between !important;
  }

  .w-100 {
    width: 100% !important;
  }

  .mb-0 {
    margin-bottom: 0 !important;
  }
  .fs-6 {
    font-size: 0.95rem !important;
  }
  .mt-3 {
    margin-top: 0.75rem !important;
  }
  .h6, h6 {
    margin: 0;
    text-transform: uppercase;
    font-size: .8125rem;
    font-weight: 600;
    letter-spacing: .08em;
    color: #95aac9;
  }

  .py-3 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }

  .align-items-center {
    align-items: center !important;
  }

  .p-4 {
    padding: 1.5rem !important;
  }

  .flex-md-row {
    flex-direction: row !important;
  }

  .py-md-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }

  .badge {
    vertical-align: middle;
  }

  .badge.bg-secondary-soft {
    color: #6e84a3;
  }

  .badge.rounded-pill {
    padding-right: .6em;
    padding-left: .6em;
  }

  .bg-secondary-soft {
    background-color: #e2e6ed !important;
  }

  .rounded-pill {
    border-radius: 50rem !important;
  }

  .badge {
    --bs-badge-padding-x: 0.5em;
    --bs-badge-padding-y: 0.33em;
    --bs-badge-font-size: 76%;
    --bs-badge-font-weight: 400;
    --bs-badge-color: #fff;
    --bs-badge-border-radius: 0.375rem;
    display: inline-block;
    padding: var(--bs-badge-padding-y) var(--bs-badge-padding-x);
    font-size: var(--bs-badge-font-size);
    font-weight: var(--bs-badge-font-weight);
    line-height: 1;
    color: var(--bs-badge-color);
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: var(--bs-badge-border-radius);
  }

  table {
    display: table;
    border-collapse: collapse;
    box-sizing: border-box;
    text-indent: initial;
    border-spacing: 2px;
    border-color: gray;
    caption-side: bottom;
  }

  tr {
    display: table-row;
    vertical-align: inherit;
    border-color: inherit;
  }

  .card-table {
    margin-bottom: 0;
    width: 100%;
    font-size: .8125rem;
    color: #12263f;
    vertical-align: top;
    border-color: #12263f;
  }

  .card {
    box-shadow: 0 0.75rem 1.5rem rgba(18, 38, 63, .03);
    position: relative;
    display: flex;
    flex-direction: column;
    min-width: 0;
    word-wrap: break-word;
    background-color: #fff;
    background-clip: border-box;
    border-radius: 1rem;
    margin: 4rem;
  }

  .table-responsive {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }

  .table > thead {
    vertical-align: bottom;
  }

  tbody, td, tfoot, th, thead, tr {
    border: 0 solid;
    border-color: inherit;
  }

  thead {
    display: table-header-group;
    vertical-align: middle;
    border-color: inherit;
  }

  tr {
    display: table-row;
    vertical-align: inherit;
    border-color: inherit;
  }

  .card-table tbody td:first-child, .card-table thead th:first-child {
    padding-left: 1.5rem !important;
  }

  .table thead th {
    background-color: #f9fbfd;
    text-transform: uppercase;
    font-size: .8125rem;
    font-weight: 600;
    letter-spacing: .08em;
    color: #95aac9;
  }

  .card-table thead th {
    border-top-width: 0;
  }

  .table thead th {
    font-size: .625rem;
  }

  .table thead th, td, tbody th {
    vertical-align: middle;
    text-align: center;
  }

  .table [data-sort], .table-nowrap td, .table-nowrap th {
    white-space: nowrap;
  }

  .table thead th {
    background-color: #f9fbfd;
    text-transform: uppercase;
    font-size: .8125rem;
    font-weight: 600;
    letter-spacing: .08em;
    color: #95aac9;
    padding: 1rem;
  }

  .text-start {
    text-align: left !important;
  }

  .card-inner-table {
    margin-top: 2rem;
  }

  .card-inner-table thead th {
    background-color: #fff;
  }

  .table td, .table th {
    border-top: 1px solid #edf2f9;
    border-bottom: 0;
    padding: 1rem;
  }

  .card-inner-table td, .card-inner-table th {
    border-top: 1px dashed #edf2f9;
  }

  .mid {
    flex: 0 0 auto;
    width: 100%;
  }

  .table > :not(caption) > * > * {
    background-color: transparent;
    border-bottom-width: 1px;
    box-shadow: inset 0 0 0 9999px transparent;
  }

  /* Nodes */
  .node_type {
    background-color: #fad7dd !important;
    color: #e63757;
    text-transform: uppercase;
    vertical-align: middle;
    padding: 0.44rem;
    border-radius: 0.375rem;
    cursor: crosshair;
  }

  /* Nodes */
  .node_type__source {
    background-color: #ccf7e5 !important;
    color: #00b368;
  }

  .node_type__transform {
    background-color: #ccefff !important;
    color: #0063b4;
  }

  .node_type__metric {
    background-color: #fad7dd !important;
    color: #a2283e;
  }

  .node_type__dimension {
    background-color: #ffefd0 !important;
    color: #a96621;
  }

  .node_type__cube {
    background-color: #ffe5c4 !important;
    color: #C21807;
  }

  .status__valid {
    color: #00b368;
  }

  .status {
    text-transform: capitalize;
    vertical-align: middle;
    text-align: center;
  }

  .align-items-center {
    align-items: center !important;
  }

  .col {
    flex: 0 1;
    padding: 1.5rem;
  }

  .col.active {
    padding-bottom: 1.315rem;
    color: #2c7be5;
    border-bottom: solid 0.2em #2c7be5;
    text-align: center;
  }
  .col.active a {
    color: #2c7be5;
  }
  .col a:hover {
    color: #2c7be5;
  }

  .row > * {
    flex-shrink: 0;
    width: 100%;
    max-width: 100%;
    padding-right: calc(var(--bs-gutter-x) * .5);
    padding-left: calc(var(--bs-gutter-x) * .5);
    margin-top: var(--bs-gutter-y);
  }

  .row {
    --bs-gutter-x: 1.5rem;
    --bs-gutter-y: 0;
    display: flex;
    flex-wrap: wrap;
  }

  .header {
    --bs-header-margin-bottom: 1.5rem;
    --bs-header-spacing-y: 1.5rem;
    --bs-header-body-border-width: 1px;
    --bs-header-body-border-color: #e3ebf6;
    --bs-header-body-border-color-dark: rgba(227, 235, 246, .1);
    height: 90px;
    transition: none;
    display: flex;
    align-items: center;
    background-color: transparent;
  }

  *, :after, :before {
    box-sizing: border-box;
  }

  .header-tabs {
    margin-bottom: calc(var(--bs-header-spacing-y) * -1);
    border-bottom-width: 0;
  }

  .nav-tabs .nav-item:first-child {
    margin-left: 0;
  }

  .nav-tabs .nav-item {
    margin-left: .75rem;
    //margin-right: .75rem;
  }

  .nav-tabs .nav-item.show .nav-link, .nav-tabs .nav-link.active {
    color: #12263f;
    background-color: transparent;
    border-color: #2c7be5;
  }

  .nav-link {
    display: block;
    color: #A1A5B7;
    transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out;
  }

  .nav-overflow {
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    padding-bottom: 1px;
  }

  pre {
    border-radius: 1rem;
    padding: 2rem;
  }

  .container {
    max-width: 1320px;
    width: 100%;
    padding-left: 30px !important;
    padding-right: 30px !important;
  }

  .logo {
    margin-right: 3.75rem !important;
    flex-grow: 0 !important;
  }

  .logo img {
    padding: 10px;
  }

  .menu-lg-row > .menu-item {
    display: flex;
    align-items: center;
  }

  .menu-item {
    display: block;
    padding: 0.15rem 0;
  }

  .me-lg-2 {
    margin-right: 0.5rem !important;
  }

  .menu, .menu-wrapper {
    display: flex;
    padding: 0;
    margin: 0;
    list-style: none;
  }

  .menu-item .menu-link {
    cursor: pointer;
    align-items: center;
    flex: 0 0 100%;
    padding: 0.65rem 1rem;
    transition: none;
    outline: none !important;
    font-family: Inter, Helvetica, sans-serif;
  }

  .menu-title a {
    color: #7E8299;
  }

  .menu-title a:hover {
    color: #3F4254;
  }

  .node__header, .mid {
    background-color: #F4F4F4;
    padding-bottom: 2rem;
  }

  .rounded-box {
    border-radius: 1rem !important;
    background-color: #ffffff;
    max-width: fit-content;
  }

  .card-header {
    align-items: center;
    margin: 0.5rem 0.5rem 0.5rem 0;
    padding: 0 2.25rem 0 2.25rem;
  }

  .text-gray-400 {
    color: #B5B5C3 !important;
  }
`;
